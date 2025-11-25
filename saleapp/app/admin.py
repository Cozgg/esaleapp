from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, expose, BaseView
from werkzeug.utils import redirect

from app import app, db
from app.models import Category, Product, UserRole
from flask_login import current_user, logout_user

admin = Admin(app=app, name='esaleappCozg')

class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__(UserRole.ADMIN)

class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')
    def is_accessible(self):
        return current_user.is_authenticated

class CategoryView(AuthenticatedView):
    # Cột hiển thị
    column_list = ['id', 'name', 'products']
    column_labels = {
        'id': 'ID',
        'name': 'Tên danh mục',
        'products': 'Sản phẩm'
    }

    # Cho phép tìm kiếm, lọc
    column_searchable_list = ['name']
    column_filters = ['name']

    # Không cho chỉnh sửa ID
    form_excluded_columns = ['products']

    # Thêm mô tả trang
    page_size = 10
    can_export = True

class ProductView(AuthenticatedView):
    column_list = ['id', 'name', 'description', 'price', 'category']
    column_labels = {
        'id': 'ID',
        'name': 'Tên sản phẩm',
        'description': 'Mô tả',
        'price': 'Giá',
        'category': 'Danh mục'
    }

    # Thêm search, filter
    column_searchable_list = ['name', 'description']
    column_filters = ['price', 'category.name']

    # Format hiển thị giá cho đẹp
    def _format_price(view, context, model, name):
        return f"{model.price:,.0f} ₫"

    column_formatters = {
        'price': _format_price
    }

    # Giới hạn số dòng trên 1 trang
    page_size = 15
    can_create = True
    can_edit = True
    can_delete = True
    edit_modal = True


    form_widget_args = {
        'description': {
            'rows': 5,
            'style': 'resize: vertical; width: 100%;'
        }
    }


admin.add_view(CategoryView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(LogoutView(name='Đăng xuất'))