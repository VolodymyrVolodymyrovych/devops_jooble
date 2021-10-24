from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    Column,
    String,
    Integer,
    Date,
    ForeignKey,
    delete
)
from sqlalchemy.orm import relationship


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://doadmin:kYugpP1bEg4Rkrzj@db-postgresql-vovusik-do-user-9931401-0.b.db.ondigitalocean.com:25060/defaultdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
client = app.test_client()

app.config.from_object(Config)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    second_name = db.Column(db.String)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

#def userr():
#    users = db.session.query(User).all()
#    return render_template("user_all.html", users=users)

@app.route('/define-data', methods=['POST', 'GET'])
def define_data():
    if request.method == "POST":
        id_ = request.form['id']
        users = db.session.query(User).get(id_)
        return render_template("output-data.html", users=users)
    return render_template("define-data.html")


@app.route('/users_all')
def users_all():
    users = db.session.query(User).all()
    return render_template("users_all.html", users=users)


@app.route('/delete-data', methods=['POST', 'GET'])
def delete_data():
    if request.method == "POST":
        id_del = request.form['id']
        users = db.session.query(User).filter_by(id=id_del).delete()
        db.session.commit()
        users = db.session.query(User).all()
        return render_template("users_all.html", users=users)
    return render_template("delete-data.html")


@app.route('/add-data', methods=['POST', 'GET'])
def add_data():
    if request.method == "POST":
        first_name_ = request.form['first_name']
        second_name_ = request.form['second_name']
        users = User(first_name=first_name_, second_name=second_name_)
        try:
            db.session.add(users)
            db.session.commit()
            return redirect("/")
        except:
            print("Error with adding data to database")
    all = db.session.query(User).all()
    return render_template("add-data.html", users=all)


@app.route('/change-data', methods=['POST', 'GET'])
def change_data():
    if request.method == "POST":
        id_ = request.form['id']
        users = db.session.query(User).get(id_)
        users.first_name = request.form['first_name']
        users.second_name = request.form['second_name']
        try:
            # users = db.session.query(User).filter_by(User.id == id_).\update({User.first_name : first_name_},\{User.second_name : second_name_},\synchronize_session=False)

            db.session.commit()
            return redirect('/')
        except:
            print("Error related with modifying data in DB")
    return render_template("change-data.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=False)
