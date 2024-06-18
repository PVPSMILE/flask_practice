import flask, os, pandas
from shop.settings import db
from shop_page.models import Product
from registration_page.models import User
from flask_login import current_user

def admin_render():
    if len(Product.query.all()) == 0:
        path = os.path.abspath(__file__ + '/../Product.xlsx')

        read_xl = pandas.read_excel(
            io= path,
            header= None,
            names = ['name', 'price', 'count', 'discount', 'description']
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

    if flask.request.method == 'POST':
        if flask.request.form.get('del'):
            product_id = int(flask.request.form['del'])
            product_del = Product.query.get(product_id)
            if product_del:
                db.session.delete(product_del)
                db.session.commit()
                os.remove(os.path.abspath(__file__ + f"/../../shop_page/static/img/{product_del.name}.png"))

        if flask.request.form.get('new-product'):
            product = Product(
                name = flask.request.form['name'],
                price = flask.request.form['price'],
                count = flask.request.form['count'],
                discount = flask.request.form['discount'],
                description = flask.request.form['description'],
                final_price = round(int(flask.request.form['price']) - (int(flask.request.form['price'])*(int(flask.request.form['discount']) / 100)), 0)
            )

            print(product.final_price)

            db.session.add(product)
            db.session.commit()

            img = flask.request.files['img']
            img.save(os.path.abspath(__file__ + f'/../../shop_page/static/img/{product.name}.png'))

        if flask.request.form.get('set-changes'):
            product_data = flask.request.form.get("set-changes").split('-') 
            product_id = int(product_data[-1])
            get_product = Product.query.get(product_id)
            abspath = os.path.abspath(__file__ + "/../../shop_page/static/img")

            if "image" == product_data[0]:
                os.remove(abspath + f'/{get_product.name}.png')
                new_image = flask.request.files['image']
                new_image.save(abspath + f'/{get_product.name}.png')
                # print('OK')

            elif 'name' == product_data[0]:
                new_product_name = flask.request.form['name']
                os.rename(src= abspath + f'/{get_product.name}.png', dst= abspath + f'/{new_product_name}.png')
                get_product.name = new_product_name
                db.session.commit()

            elif 'price' == product_data[0]:
                new_product_price = flask.request.form['price']
                get_product.price = new_product_price

                get_product.final_price = round(int(new_product_price) - (int(new_product_price)*(int(get_product.discount) / 100)), 0)
                db.session.commit()

            elif 'discount' == product_data[0]:
                new_product_discount = flask.request.form['discount']
                get_product.discount = new_product_discount

                get_product.final_price = round(int(get_product.price) - (int(get_product.price)*(int(new_product_discount) / 100)), 0)
                db.session.commit()

    if current_user.is_authenticated:
        return flask.render_template(
            template_name_or_list = 'admin.html', 
            products = Product.query.all(),
            is_auth = current_user.is_authenticated,
            name = current_user.name,
            is_admin = current_user.is_admin
        )

    # return flask.render_template("admin.html", products = Product.query.all(), name = current_user.name)
