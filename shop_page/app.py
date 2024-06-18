import flask

shop_page = flask.Blueprint(
    name = 'shop_page',
    import_name= 'shop_page',
    template_folder= 'templates',
    static_folder= 'static',
    static_url_path= '/shop_page/'
)