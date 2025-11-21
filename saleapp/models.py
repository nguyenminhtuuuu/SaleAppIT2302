import json
from xmlrpc.client import DateTime
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime, Enum, Text
from sqlalchemy.orm import relationship
from saleapp import  db, app
from flask_login import UserMixin
from enum import Enum as RoleEnum

class UserEnum(RoleEnum):
    USER = 1
    ADMIN = 2

class Base(db.Model):
    __abstract__=True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    def __str__(self):
        return self.name

class User(Base, UserMixin):
    username = Column(String(150), unique=True, nullable=False)
    password = Column(String(150), unique=False)
    avatar = Column(String(300), default= "https://bla.edu.vn/wp-content/uploads/2025/09/avatar-fb.jpg")
    role = Column(Enum(UserEnum), nullable=False, default=UserEnum.USER)

class Category(Base):
    products = relationship('Product', backref="category", lazy=True)

class Product(Base):
    image = Column(String(300), default="https://images-na.ssl-images-amazon.com/images/I/61aOEheWDOL.jpg")
    price = Column(Float, default=0.0)
    cate_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    description = Column(Text)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        c1 = Category(name="laptop")
        # print(c1)
        c2 = Category(name="Mobile")
        c3 = Category(name="Tablet")

        db.session.add_all([c1,c2,c3])

        with open("data/product.json", encoding="utf-8") as f:
            products = json.load(f)

            for p in products:
                db.session.add(Product(**p))

        import hashlib
        u = User(name="User", username="user", password=str(hashlib.md5("123".encode("utf-8")).hexdigest()))

        db.session.add(u)
        db.session.commit()