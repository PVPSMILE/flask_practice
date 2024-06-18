import flask, os, json
from registration_page import User  
from flask_login import login_user, current_user


def show_login():
    # if flask.request.method == 'POST':
    #     for user in User.query.filter_by(name = flask.request.form['name']):
    #         if user.password == flask.request.form['password']:
    #             login_user(user)
    #             return flask.redirect('/shop_page/')
            
    #     return "Пароль вказано неправильно"

    path = os.path.abspath(__file__ + '/../static/json/login.json')
    with open(path, 'r', encoding='utf-8') as file:
        data_dict = json.load(file)

    # return flask.render_template(template_name_or_list='login.html', content=data_dict['content'], is_auth = current_user.is_authenticated)

    if flask.request.method == 'POST':
        for user in User.query.filter_by(name = flask.request.form['name']):
            if user.password == flask.request.form['password']:
                login_user(user)
                
    
    if not current_user.is_authenticated:
        return flask.render_template(template_name_or_list= 'login.html', content=data_dict['content'])
    return flask.redirect('/')
