from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def receive_data():
    if request.method == 'POST':
        return do_the_login(username=request.form['username'], password=request.form['password'])
    
def do_the_login(username, password):
    if username == 'a' and password == 'b':
        print("ACERTOU")
        return render_template("login.html", login_username=username, login_password=password)
    else:
        print("ERROU")
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)