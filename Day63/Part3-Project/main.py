from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(250), nullable=False)
    author: Mapped[str] = mapped_column(db.String(250), nullable=False)
    rating: Mapped[float]= mapped_column(db.Float, nullable=False)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

with app.app_context():
    db.create_all()

# book = Book(
#     title="Harry Potter",
#     author="J. K. Rowling",
#     rating=9.3
# )

# with app.app_context():
#     db.session.add(book)
#     db.session.commit()



@app.route('/')
def home():
    result = db.session.execute(db.select(Book))
    all_books = result.scalars().all()
    return render_template("index.html", books=all_books)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(
            title = request.form.get('title'),
            author = request.form.get('author'),
            rating = float(request.form.get('rating'))
        )
        db.session.add(new_book)
        db.session.commit()

        print("Successfully added new book.")

    return render_template("add.html")

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    book_to_edit = db.get_or_404(Book, id)

    if request.method == 'POST':
        book_to_edit.rating = float(request.form.get('new_rating'))
        db.session.commit() 
    
        return redirect(url_for('home'))

    return render_template("edit.html", book=book_to_edit)


@app.route("/delete/<int:id>")
def delete(id):
    book_to_delete = db.get_or_404(Book, id)
    
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
