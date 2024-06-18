# import flask, os, json
# from .models import User
# from shop.settings import db
# from flask_login import current_user

# def reg_render():
#     global is_registration
#     is_registration = False
#     print(is_registration)
#     if flask.request.method == 'POST':
#         # user = User(
#         #     name = flask.request.form['name'],
#         #     email = flask.request.form['email'],
#         #     password = flask.request.form['password'],
#         #     password_confirmation = flask.request.form['password_confirmation'],

#         #     is_admin = False
#         # )
#         # try:
#         #     if user.password == user.password_confirmation:
#         #         db.session.add(user)
#         #         db.session.commit()
            
#         #         return flask.redirect('/authorization_page/')
#         #     else:
#         #         print("Пароль і підтвердження пароля не співпадають")
            
#         # except:
#         #     return "ERROR"

#         try:
#             user = User(
#             name = flask.request.form['name'],
#             email = flask.request.form['email'],
#             password = flask.request.form['password'],
#             password_confirmation = flask.request.form['password_confirmation'],

#             is_admin = False
#         )
#             if user.password == user.password_confirmation:
#                 db.session.add(user)
#                 db.session.commit()

#                 # is_registration = True
#                 # print(is_registration)

#                 # return flask.redirect('/authorization_page/')
            
#             # if is_registration:
#             #     return flask.redirect('/authorization_page/')


#             else:
#                 print("Пароль і підтвердження пароля не співпадають")

#         except Exception as e:
#             print(e)

    # path = os.path.abspath(__file__ + '/../static/json/reg.json')
    # with open(path, 'r', encoding = 'utf-8') as file:
    #     data_dict = json.load(file)

#     return flask.render_template(template_name_or_list = "reg.html", content = data_dict['content'],  is_auth = current_user.is_authenticated)



import flask, os, json
from shop.settings import db
from flask_login import current_user
from .models import User

def reg_render():
    is_registration = False

    if flask.request.method == "POST":
        try:
            user = User(
                name = flask.request.form['name'],
                email = flask.request.form['email'],
                password = flask.request.form['password'],
                password_confirmation = flask.request.form['password_confirmation'],

                is_admin = False
            )

            db.session.add(user)
            db.session.commit()
            is_registration = True
            # return flask.redirect('/authorization_page/')

        except Exception as e:
            print(e)

    path = os.path.abspath(__file__ + '/../static/json/reg.json')
    with open(path, 'r', encoding = 'utf-8') as file:
        data_dict = json.load(file)

    if not current_user.is_authenticated:
        return flask.render_template(template_name_or_list= 'reg.html', is_registration= is_registration, content = data_dict['content'])
    else:
        print('auth')
        return flask.redirect('/authorization_page/')
