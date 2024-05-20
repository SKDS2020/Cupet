import pandas as pd
from flask_migrate import Migrate
from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
# from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secret key for session security
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'


db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    race = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    fits_for = db.Column(db.String(20), unique=False, nullable=False)
    img_path1 = db.Column(db.String(100), unique=False, nullable=False)
    img_path2 = db.Column(db.String(100), unique=False, nullable=False)
    img_path3 = db.Column(db.String(100), unique=False, nullable=False)



@app.route("/category")
def category():
    c_pets=Pet.query.all()
    return render_template("category.html", pets=c_pets)

@app.route("/")
def hi():
    return redirect('/signin')

@app.route("/pet/<int:pet_id>")
def pet(pet_id):
    pets=Pet.query.all()
    return render_template("criminal.html", selected_pet=pets[pet_id])

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect('/category')
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            return redirect('/category')
    return render_template('signin.html')

@app.route('/signout')
def signout():
    session.pop('user_id', None)
    return redirect('/')


if __name__ == '__main__':
    with app.app_context():
        df = pd.read_csv('petsdata.csv')
        df2 = pd.read_csv('usersdata.csv')
        print(df)
        df.to_sql(name='pet', con=db.engine, if_exists='replace')
        df2.to_sql(name='user', con=db.engine, if_exists='replace')

    app.run(host="0.0.0.0", port=5001, debug=True)

