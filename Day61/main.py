from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
import email_validator
from flask_bootstrap import Bootstrap5

class LoginForm(FlaskForm):
    email = StringField("name", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Log In")

app = Flask(__name__)
app.config['SECRET_KEY'] = "your-testing-key-123"

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): 
        email = form.email.data
        password = form.password.data
        
        if email == "admin@email.com" and password == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
            
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
