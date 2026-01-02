from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired
import requests
import json

with open("sensitive_data.json") as f:
    sensitive_data = json.load(f)

tmdb_api_token = sensitive_data["tmdb"]["api_token"]

TMDB_HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {tmdb_api_token}"
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(db.Integer, nullable=False)
    description: Mapped[str]= mapped_column(db.String(500), nullable=False)
    rating: Mapped[float]= mapped_column(db.Float, nullable=True)
    ranking: Mapped[int]= mapped_column(db.Integer, nullable=True)
    review: Mapped[str]= mapped_column(db.String(500), nullable=True)
    img_url: Mapped[str]= mapped_column(db.String, nullable=False)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my-top-movies.db"
db.init_app(app)

with app.app_context():
    db.create_all()

    movie_exists = db.session.execute(db.select(Movie).where(Movie.title == "Hoi")).scalar()
    if not movie_exists:
        new_movie = Movie(
            title="Hoi",
            year=2024,
            description="OiOIOIiOIoioioi",
            rating=10,
            ranking=2,
            review="My favourite movie.",
            img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
        )
        db.session.add(new_movie)
        db.session.commit()

    movie_exists = db.session.execute(db.select(Movie).where(Movie.title == "Phone Booth")).scalar()
    if not movie_exists:
        new_movie = Movie(
            title="Phone Booth",
            year=2002,
            description="Publicist Stuart Shepard finds himself trapped...",
            rating=7.3,
            ranking=10,
            review="My favourite character was the caller.",
            img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
        )
        db.session.add(new_movie)
        db.session.commit()

class EditForm(FlaskForm):
    rating = FloatField('New Rating', validators=[DataRequired()])
    review = StringField('New review', validators=[DataRequired()])
    submit = SubmitField('Update')

class SearchForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Search Movie')

class AddForm(FlaskForm):
    year = IntegerField('Year', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])
    ranking = IntegerField('Ranking', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    img_url = StringField('Image URL', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
    movies = result.scalars().all()
    print(movies)
    for i in range(len(movies)):
        movies[i].ranking = i+1
    db.session.commit()

    return render_template("index.html", movies=movies)

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    edit_form = EditForm()
    if edit_form.validate_on_submit():
        book_to_edit = db.get_or_404(Movie, id)
        book_to_edit.rating = edit_form.rating.data
        book_to_edit.review = edit_form.review.data
        db.session.commit() 
    
        return redirect(url_for('home'))
    
    return render_template("edit.html", form=edit_form)

@app.route("/delete/<int:id>", methods=['GET', 'POST'])
def delete(id):
    book_to_delete = db.get_or_404(Movie, id)
    db.session.delete(book_to_delete)
    db.session.commit() 

    return redirect(url_for('home'))

@app.route("/add", methods=['GET', 'POST'])
def search():
    search_form = SearchForm()
    if search_form.validate_on_submit():
        
        searched_title = search_form.title.data
        params = {
            "query": searched_title
        }

        response = requests.get(url="https://api.themoviedb.org/3/search/movie", headers=TMDB_HEADERS, params=params)
        movies_found = response.json()
    
        return render_template("select.html", movies=movies_found["results"])
    return render_template("add.html", form=search_form)

@app.route("/add/<tmdb_id>", methods=['GET', 'POST'])
def add(tmdb_id):
    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{tmdb_id}", headers=TMDB_HEADERS)
    movie = response.json()

    movie_to_add = Movie(
        title = movie["title"],
        year = movie["release_date"][:4],
        description = movie["overview"],
        rating = None,
        ranking = None,
        review = None,
        img_url = f"https://image.tmdb.org/t/p/w500{movie["poster_path"]}"
    )
    db.session.add(movie_to_add)
    db.session.commit()

    return redirect(url_for('edit', id=movie_to_add.id))

if __name__ == '__main__':
    app.run(debug=True)
