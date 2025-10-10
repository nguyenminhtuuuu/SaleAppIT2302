from itertools import product

from flask import Flask, render_template, request
from saleapp import dao

app = Flask(__name__)


@app.route("/")

def index():
    q = request.args.get("q")
    cate = request.args.get("cate")
    cates = dao.load_category()
    products = dao.load_product(q = q, cate = cate)
    return render_template("index.html", cates= cates, products=products)

@app.route("/products/<int: id>")
def details(id):

    return render_template("product-details.html")
if __name__ == "__main__":
    app.run(debug=True)