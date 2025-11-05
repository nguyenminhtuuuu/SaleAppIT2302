from itertools import product
import math
from flask import Flask, render_template, request
from saleapp import dao
from saleapp import app


@app.route("/")

def index():
    q = request.args.get("q")
    cate = request.args.get("cate")
    products = dao.load_product(q = q, cate = cate) #cate = cate_id
    pages = math.ceil(dao.count_product()/3)
    return render_template("index.html", products=products, pages = pages)

@app.route("/products/<int:id>")  #int: kieu du lieu, id: ten tham so
def details(id):
    prod = dao.get_product_by_id(id)
    return render_template("product-details.html", prod = prod)

@app.context_processor
def common_attribute():
    return{
        "cates": dao.load_category() #bien toan cuc
    }

if __name__ == "__main__":
    app.run(debug=True)