
from app.models import Category, Product


def get_all_cates():
    return Category.query.all()

def get_all_prod(kw = None, category_id = None):

    products = Product.query

    if category_id:
        products = products.filter(Product.category_id == category_id)

    if kw:
        products = products.filter(Product.name.contains(kw))

    return products.all()