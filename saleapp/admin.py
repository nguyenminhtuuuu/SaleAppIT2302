from flask_admin import Admin
from flask_admin.theme import Bootstrap4Theme
from flask_admin.contrib.sqla import ModelView
from saleapp import app, db
from models import Category, Product

admin = Admin(app=app, name ="E-COMMERCE", theme=Bootstrap4Theme())


class MyCategoryView(ModelView):
    column_list = ["name", "products"]
    column_searchable_list = ['name']

admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(ModelView(Product, db.session))