from flask import Flask, render_template, url_for
import requests
from post import Post

app = Flask(__name__)
post = Post()

@app.route('/')
def home():
    return render_template("index.html", posts=post.all_posts)

@app.route('/post/<int:id>')
def get_blog(id):
    return render_template("post.html", posts=post.all_posts, post_id=id)

if __name__ == "__main__":
    app.run(debug=True)
