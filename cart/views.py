import flask
from flask_login import current_user
from shop_page.models import Product

def cart_render():
    is_admin = False
    products_cookie = flask.request.cookies.get('products')
    
    if products_cookie:
        products = products_cookie.split(' ')
        list_products = []
        repeate_id = []

        for id_product in products:
            count_products = products.count(id_product)
            if id_product not in repeate_id:
                product = Product.query.get(id_product)
                if product:
                    product.count = count_products
                    list_products.append(product)
                    repeate_id.append(id_product)

        # if current_user.is_authenticated:
        #     return flask.render_template('cart.html', products= list_products, name= current_user.name, is_admin = current_user.is_admin, is_authenticated = current_user.is_authenticated)

        if current_user.is_authenticated:
            print(48932)
            return flask.render_template(
                template_name_or_list = 'cart.html',
                products= list_products,
                is_authenticated = current_user.is_authenticated,
                name = current_user.name,
                is_admin = current_user.is_admin
            )
        
        print('no auth')
        return flask.render_template(
            template_name_or_list = 'cart.html',
            is_admin = current_user.is_admin
        )
        
    else:
        print("No products found in cookies.")
        return flask.render_template('cart.html', name=current_user.name)
