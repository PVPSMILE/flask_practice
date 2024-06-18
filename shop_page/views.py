import flask, os, pandas
from shop.settings import db
from .models import Product

from registration_page.models import User

# from registration_page.views import user

from flask_login import current_user

def shop_render():
    if len(Product.query.all()) == 0:
        path = os.path.abspath(__file__ + '/../Product.xlsx')

        read_xl = pandas.read_excel(
            io= path,
            header= None,
            names = ['name', 'price', 'count', 'discount', 'description', 'final_price']
        )

        for row in read_xl.iterrows():
            data_row = row[1]

            product = Product(
                name = data_row['name'],
                price = data_row['price'],
                count = data_row['count'], 
                discount = data_row['discount'], 
                description = data_row['description'], 
                final_price = data_row['final_price']
            )
            db.session.add(product)
        db.session.commit()

    is_admin = False
    if current_user.is_authenticated:
        return flask.render_template(
            template_name_or_list = "shop.html", 
            products = Product.query.all(),
            is_auth = current_user.is_authenticated,
            name = current_user.name,
            is_admin = current_user.is_admin
        )
    return flask.render_template(
        template_name_or_list = "shop.html", 
        products = Product.query.all(), 
        is_admin = is_admin
    )
    # return flask.render_template("shop.html", products = Product.query.all(), name = current_user.name, is_admin = current_user.is_admin)
