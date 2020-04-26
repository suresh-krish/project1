from datetime import datetime as dt
import os
from flask import Flask, session,request,render_template,flash,logging,redirect,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
import csv
from datetime import datetime as dt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://sjdihkgayawirr:6d55f7ffac9a770752523bf08b31b8384cd95cbd63f1f936776c410e85406118@ec2-34-200-72-77.compute-1.amazonaws.com:5432/d7tbt9n8q5pp5m'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db= SQLAlchemy()



class Books(db.Model):
    __tablename__="books"
    isbn=db.Column(db.String,primary_key=True)
    title=db.Column(db.String,nullable=False)
    author=db.Column(db.String,nullable=False)
    year=db.Column(db.String,nullable=False)

    def __init__(self,isbn,title,author,year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

def main():
    db.create_all()
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn,title,author,year in reader:
        book = Books(isbn=isbn, title=title, author=author,year=year)
        db.session.add(book)
        print(f"Added book of year {year} ,isbn: {isbn},title: {title} ,author: {author}.")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()



class User(db.Model):
    __tablename__ = "user"
    time=db.Column(db.DateTime,nullable=False)
    email = db.Column(db.String(120),primary_key=True)
    password = db.Column(db.String(80),nullable=False)

    def __init__(self,email,password):
        self.email = email
        self.password=password
        self.time=dt.now()