from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(250))
    name: Mapped[str] = mapped_column(String(1000))



with app.app_context():
    db.create_all()
    
    # db.session.add(new_user)
    # db.session.commit()


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed_password = generate_password_hash(password=request.form.get('password'), method="pbkdf2:sha256", salt_length=8)
        new_user = User(
            email=request.form.get('email'),
            password=hashed_password,
            name=request.form.get('name')
        )
        user_exists = db.session.execute(db.select(User).where(User.email == new_user.email)).scalar()
        if user_exists:
            flash("User already exists. Please login.")
            return redirect(url_for('register')) 
        else:
            db.session.add(new_user)
            db.session.commit()

            if login_user(new_user):
                flash('Logged in successfully.')
                return render_template("secrets.html", name=new_user.name)


    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        email=request.form.get('email')
        password=request.form.get('password')
        
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if not user:
            flash('Email was not found. Please register.')
            return redirect(url_for('login'))
        
        elif not check_password_hash(user.password, password):
            flash("Wrong email or password.")
            return redirect(url_for('login'))

        else:
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('secrets', name=user.name))


    return render_template("login.html")


@app.route('/secrets?<name>')
@login_required
def secrets(name):
    return render_template("secrets.html", name=name)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
