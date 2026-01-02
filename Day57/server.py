from flask import Flask, render_template
import random
import datetime
import requests

AGIFY_API = "https://api.agify.io"
GENDERIZE_API = "https://api.genderize.io"

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, curr_year=datetime.date.today().year)

@app.route('/guess/<name>')
def guess(name):
    params = {
        "name": name,
    }
    response = requests.get(url=AGIFY_API, params=params)
    predicted_age = response.json()["age"]
    response = requests.get(url=GENDERIZE_API, params=params)
    predicted_gender = response.json()["gender"]
    return render_template("predictions.html",name=name.title(),predicted_age=predicted_age,predicted_gender=predicted_gender)

@app.route('/blog/<num')
def get_blog():
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("blogs.html",posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)