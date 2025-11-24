import math
from flask import render_template, request, redirect
from saleapp import app, login, admin
from saleapp import dao
from flask_login import login_user, current_user, logout_user

@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    page = request.args.get("page")
    products = dao.load_product(q=q, cate_id=cate_id, page=page)  # cate = cate_id
    pages = math.ceil(dao.count_product() / app.config["PAGE_SIZE"])
    return render_template("index.html", products=products, pages=pages)


@app.route("/products/<int:id>")  # int: kieu du lieu, id: ten tham so
def details(id):
    prod = dao.get_product_by_id(id)
    return render_template("product-details.html", prod=prod)


@app.context_processor
def common_attribute():
    return {
        "cates": dao.load_category()  # bien toan cuc
    }

@app.route("/login", methods=['get', 'post'])
def login_my_user():

    if current_user.is_authenticated: # nếu đã đăng nhập rồi thì trả về trang chủ luôn
        return redirect("/")

    err_msg = None

    if request.method.__eq__("POST"):
        username = request.form.get("username")
        password = request.form.get("password")

        user = dao.auth_user(username, password)

        if user:
            login_user(user)
            return redirect("/")

        else: # đăng nhập không thành công
            err_msg = "Tài khoản hoặc mật khẩu không đúng!"

    return render_template("login.html", err_msg=err_msg)


@app.route("/logout")
def logout_my_user():
    logout_user()
    return redirect("/login")

@app.route("/register")
def register():
    return render_template("register.html")


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

@app.route('/admin-login', methods=['post'])
def admin_login_process():
    username = request.form.get("username")
    password = request.form.get("password")

    user = dao.auth_user(username, password)

    if user:
        login_user(user)
        return redirect("/admin")

    else:  # đăng nhập không thành công
        err_msg = "Tài khoản hoặc mật khẩu không đúng!"




if __name__ == "__main__":
    app.run(debug=True, port = 5000)
