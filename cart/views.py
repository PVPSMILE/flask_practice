import flask
from flask import request, render_template, redirect
from flask_login import current_user
from shop_page.models import Product
from shop.settings import shop

from flask_mail import Mail, Message




mail = Mail(shop)


def cart_render():
    is_admin = False
    products_cookie = flask.request.cookies.get('products')
    
    if products_cookie:
        products = products_cookie.split(' ')
        list_products = []
        repeate_id = []
        total = 0

        for id_product in products:
            count_products = products.count(id_product)
            if id_product not in repeate_id:
                product = Product.query.get(id_product)
                if product:
                    product.count = count_products
                    list_products.append(product)
                    repeate_id.append(id_product)
                total += count_products * round(product.price * (1- product.discount/100))

        
        if current_user.is_authenticated:
            if request.method == 'POST':
                recipient = current_user.email  # Здесь указываете адрес получателя
                subject = 'Пример HTML-таблицы в письме'

                # Загрузка HTML-таблицы из файла send_table.html
            
                html_body = render_template('send_table.html', products=list_products, total = total)

                msg = Message(subject, recipients=[recipient])
                msg.html = html_body

                try:
                    mail.send(msg)
                except Exception as e:
                    return str(e)
                
            return flask.render_template(
                template_name_or_list = 'cart.html',
                products= list_products,
                is_authenticated = current_user.is_authenticated,
                name = current_user.name,
                is_admin = current_user.is_admin,
                total = total
            )
        
        print('no auth')
        return flask.render_template(
            template_name_or_list = 'cart.html',
            is_admin = current_user.is_admin
        )
        
    else:
        print("No products found in cookies.")
        return flask.render_template('cart.html', name=current_user.name)
