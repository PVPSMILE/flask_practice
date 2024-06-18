import flask, flask_sqlalchemy, flask_migrate, os


shop = flask.Flask(
    import_name= "settings", 
    template_folder= "shop/templates",
    instance_path= os.path.abspath(__file__ + "/.."),
    static_url_path= '/shop/'
)

shop.config['MAIL_SERVER'] = 'smtp.gmail.com' 
shop.config['MAIL_PORT'] = 587 
shop.config['MAIL_USE_TLS'] = True 
shop.config['MAIL_USE_SSL'] = False  
shop.config['MAIL_USERNAME'] = 'yarikcement@gmail.com'
shop.config['MAIL_PASSWORD'] = 'vbgh whvc dxqt ucxy'  
shop.config['MAIL_DEFAULT_SENDER'] = ('Арем', 'yarikcement@gmail.com')  
shop.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = flask_sqlalchemy.SQLAlchemy(app= shop)
migrate = flask_migrate.Migrate(app= shop, db= db)


