from flask import Flask, render_template
import requests

app=Flask(__name__)

response = requests.get(url="https://api.npoint.io/1370b90b0d657474eca7")
posts = response.json()

@app.route("/")
def home():
    return render_template("index.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:id>")
def post(id):   
    post = {}
    for p in posts:
        if p["id"] == id:
            post = p
    return render_template("post.html", post=post)


if __name__== "__main__" :
    app.run(debug=True)