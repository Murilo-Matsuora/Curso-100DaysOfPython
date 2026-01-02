import random
from flask import Flask

CORRECT_NUMBER = random.randint(0, 9)

app = Flask(__name__)

@app.route("/")
def main_page():
    return "Go to the url and type '/{your_guess}'"

@app.route("/<int:guess>")
def guess_number(guess):
    diff = CORRECT_NUMBER - guess
    if diff < 0:
        return "<h1>Too high!</h1>" \
            "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWY1dHZ2Y2Jra3d3cjE0aTUyeWRlenh4bjU2bWJxdWRyMTZuOHAzbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3BRDkVjKikYW4/giphy.gif'/>"
    if diff == 0:
        return "<h1>You got it!</h1>" \
            "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExancybDZpb3dhdGU0N216azVmaW4zNTVrMjE1bG43bGxjb3k4dWYzZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7PnYpJ2TFMygq07wWA/giphy.gif'/>"
    if diff > 0:
        return "<h1>Too low!</h1>" \
            "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTc0dHhkYXBlbGkwcWFqcWVybWRtZG9iY3AxMmVnajl2NGVzcDlubyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8yND5ned7Wft2polnB/giphy.gif'/>"

if __name__ == "__main__":
    app.run(debug=True)