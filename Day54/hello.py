from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/bye")
def bye():
    return "Bye, World!"

@app.route("/username/<name>")
def greet(name):
    return f"Hello, {name + 1}!"    

if __name__ == "__main__":
    app.run(debug=True)