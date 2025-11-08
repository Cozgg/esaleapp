from flask import render_template, request, redirect
from flask_login import login_user, logout_user

from app import app, utils, login
from app.dao import is_auth
from app.models import Category, Product, User


@app.route('/')
def index():
    categories = utils.get_all_cates()
    products = utils.get_all_prod(kw = request.args.get('key'), category_id= request.args.get('category_id'))
    return render_template("index.html", categories = categories, products = products)


@login.user_loader
def load_user(user_id):
    return utils.get_user_by_id(user_id)

@app.route("/login-admin", methods = ['GET', 'POST'])
def login_process():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = is_auth(username = username, password=password)
        if user:
            login_user(user=user)
            next = request.args.get('next')
        return redirect("/" if next is None else next)

@app.route("/logout")
def logout_process():
    logout_user()
    return redirect('/login')

if __name__ == "__main__":
    from app import admin
    app.run(debug=True)
