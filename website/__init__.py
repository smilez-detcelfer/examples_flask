from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdflwefDKLFJSWFSDFLWiov'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:OneTwoPost123@192.168.1.11:5432/supersms-test'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .models import User

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

