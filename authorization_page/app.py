import flask

login = flask.Blueprint(
    name= 'login',
    import_name= 'authorization_page',
    template_folder= 'templates',
    static_folder= 'static',
    static_url_path= '/authorization/'
)