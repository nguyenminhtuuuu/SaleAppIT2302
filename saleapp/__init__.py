from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary



app = Flask(__name__)

app.secret_key="ad4as5d4as786iuoigy" # mã ngẫu nhiên để nó thực hiện chuyện bảo mật của nó
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:root@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 3
db = SQLAlchemy(app)

cloudinary.config(cloud_name='deeqcwnpm',
                  api_key='642514279843968',
                  api_secret='iOM3oFrZpEwBIrnkHdaPfmT8njY',)

login = LoginManager(app)