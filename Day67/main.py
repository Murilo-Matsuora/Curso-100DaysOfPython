from flask import Flask, render_template, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date, datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

ckeditor = CKEditor(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

class AddPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    img_url = StringField('Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField('Body', validators=[DataRequired()]) 
    submit = SubmitField('Post')


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost))
    return render_template("index.html", all_posts=posts.scalars().all())

@app.route('/post/<post_id>')
def show_post(post_id):
    try:
        requested_post = db.session.get(BlogPost, post_id)
    except AttributeError:
        return jsonify(error={"Not Found": f"Sorry, no post with id {post_id} was not found in the database."}), 404
    else:
        return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/add', methods=['GET', 'POST'])
def add_new_post():
    form = AddPostForm()
    if form.validate_on_submit():
        formatted_date = date.today().strftime("%B %d, %Y")
        new_post = BlogPost(
            title = form.title.data,
            subtitle = form.subtitle.data,
            date = formatted_date,
            body = form.body.data,
            author = form.author.data,
            img_url = form.img_url.data
        )

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('get_all_posts'))

    return render_template("make-post.html", form=form, edit=False)

# TODO: edit_post() to change an existing blog post
@app.route('/edit/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post_to_edit = db.session.get(BlogPost, post_id)

    form = AddPostForm(obj=post_to_edit)

    if form.validate_on_submit():
        
        print("\n\n")
        print(form.body.data)
        print("\n\n")

        post_to_edit.title = form.title.data
        post_to_edit.subtitle = form.subtitle.data
        post_to_edit.body = form.body.data
        post_to_edit.author = form.author.data
        post_to_edit.img_url = form.img_url.data
        
        db.session.commit()

        return redirect(url_for('show_post', post_id=post_to_edit.id))

    return render_template("make-post.html", form=form, edit=True)

# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<post_id>', methods=['GET', 'POST'])
def delete_post(post_id):
    post_to_delete = db.session.get(BlogPost, post_id)

    db.session.delete(post_to_delete)
    db.session.commit()

    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
