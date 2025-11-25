import cloudinary
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'sdasdghkwgrkygfda83497dad!#!#R3r2g343R$@#42'

app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:root@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 8

db = SQLAlchemy(app)
login = LoginManager(app = app)


cloudinary.config(cloud_name='dp6npbtxz',
                  api_key='892228849187776',
                  api_secret='eAH7b_PTAYJ3zmgHatN10BY-u8M')