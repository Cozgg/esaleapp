from flask import render_template, request

from app import app, utils
from app.models import Category, Product


@app.route('/')
def index():
    categories = utils.get_all_cates()
    products = utils.get_all_prod(kw = request.args.get('key'), category_id= request.args.get('category_id'))
    return render_template("index.html", categories = categories, products = products)


if __name__ == "__main__":
    app.run(debug=True)
