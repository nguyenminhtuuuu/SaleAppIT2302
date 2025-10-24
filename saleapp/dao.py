import json
from models import Category, Product


def load_category():
    # with open("data/category.json", encoding="utf-8") as f:
    #     return json.load(f)
    return Category.query.all()


def load_product(q = None , cate = None):
    # with open("data/product.json", encoding="utf-8") as f:
    #     products = json.load(f)
    #
    #     if q:
    #         products = [p for p in products if p["name"].find(q) >= 0]
    #     if cate:
    #          products = [p for p in products if p["cate_id"].__eq__(int(cate))]
    #     return products
    query = Product.query

    if q:
        query = query.filter(Product.name.contains(q))

    if cate:
        query = query.filter(Product.cate_id.__eq__(cate))

    return query.all()

def get_product_by_id(id):
    # with open("data/product.json", encoding="utf-8") as f:
    #     products = json.load(f)
    #     for p in products:
    #         if p["id"].__eq__(id):
    #             return p

    return Product.query.get(id)


if __name__ == "__main__":
    print(get_product_by_id(1))
