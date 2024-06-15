import flask, flask_sqlalchemy, flask_migrate, os


shop = flask.Flask(
    import_name= "settings", 
    template_folder= "shop/templates",
    instance_path= os.path.abspath(__file__ + "/.."),
    static_url_path= '/shop/'
)

shop.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = flask_sqlalchemy.SQLAlchemy(app= shop)
migrate = flask_migrate.Migrate(app= shop, db= db)


