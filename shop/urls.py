from .settings import shop
from home_page import home, home_render
from registration_page import registration, reg_render
from authorization_page import login, show_login
from shop_page import shop_page, shop_render
from cart import cart, cart_render
from admin_page import admin, admin_render


home.add_url_rule(rule= "/", view_func= home_render, methods = ['GET', 'POST'])
registration.add_url_rule(rule= '/registration_page/', view_func= reg_render, methods = ['GET', 'POST'])
login.add_url_rule(rule= '/authorization_page/', view_func= show_login, methods = ['GET', 'POST'])
shop_page.add_url_rule(rule='/shop_page/', view_func= shop_render, methods = ['GET', 'POST'])
cart.add_url_rule(rule= '/cart/', view_func= cart_render, methods = ['GET', 'POST'])

admin.add_url_rule(rule= '/admin/', view_func= admin_render, methods = ['GET', 'POST'])


shop.register_blueprint(blueprint= home)
shop.register_blueprint(blueprint= registration)
shop.register_blueprint(blueprint= login)
shop.register_blueprint(blueprint= shop_page)
shop.register_blueprint(blueprint= cart)
shop.register_blueprint(blueprint= admin)