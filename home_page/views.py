import flask
from flask_login import current_user, logout_user


def home_render():

    # if flask.request.method == "POST":
    #     if current_user.is_authenticated:
    #         logout_user()
    #         flask.redirect('/shop_page/')
    # try:
    #     return flask.render_template(template_name_or_list= 'home.html', is_auth = current_user.is_authenticated, name = current_user.name, is_admin = current_user.is_admin)
    # except:
    #     return flask.redirect('/registration_page/')
    
    if current_user.is_authenticated:
        return flask.render_template(
            template_name_or_list= "home.html", 
            is_auth = current_user.is_authenticated,
            name = current_user.name,
            is_admin = current_user.is_admin
        )
    return flask.render_template(template_name_or_list= "home.html")



