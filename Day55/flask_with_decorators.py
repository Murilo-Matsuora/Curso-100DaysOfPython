from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def make_emphasis(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper

def make_undelined(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/bye")
@make_bold
@make_emphasis
@make_undelined
def bye():
    return "Bye, World!"

if __name__ == "__main__":
    app.run(debug=True)