from flask import Flask
from flask_migrate import Migrate

from config import DevelopmentConfig
from app.extensions import db

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate = Migrate(app, db)

    migrate.init_app(app, db)


    @app.route("/")
    def index():
        return "Test"
    
    return app
