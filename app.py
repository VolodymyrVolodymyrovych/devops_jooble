from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    Column,
    String,
    Integer,
    Date,
    ForeignKey,
)
from sqlalchemy.orm import relationship


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://doadmin:kYugpP1bEg4Rkrzj@db-postgresql-vovusik-do-user-9931401-0.b.db.ondigitalocean.com:25060/defaultdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
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


@app.route('/users/<int:id>')
def userr_current(id):
    users = db.session.query(User).get(id)
    return render_template("user_current.html", users=users)

if __name__ == "__main__":
    app.run(debug=False)
