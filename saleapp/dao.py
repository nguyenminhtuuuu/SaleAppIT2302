import json

def load_category():
    with open("data/category.json", encoding="utf-8") as f:
        cates = json.load(f)
        return cates


def load_product(q = None , cate = None):
    with open("data/product.json", encoding="utf-8") as f:
        products = json.load(f)

        if q:
            products = [p for p in products if p["name"].find(q) >= 0]
        if cate:
             products = [p for p in products if p["cate_id"].__eq__(int(cate))]
        return products

def get_product_by_id(id):
    with open("data/product.json", encoding="utf-8") as f:
        products = json.load(f)
        for p in products:
            if p["id"].__eq__(id):
                return p

    return None


if __name__ == "__main__":
    print(get_product_by_id(1))
