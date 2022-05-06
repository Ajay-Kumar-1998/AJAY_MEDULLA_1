from flask import Flask
from flask_login import LoginManager, login_manager
from flask_restful import Api

from os import path
from flask_cors import CORS
# from flask_mail import Mail,Message
# from flask_caching import Cache 
from flask_caching import Cache

#-------------initialization-------------------
# db = SQLAlchemy()
# data_base= "final_project.sqlite3"

#---------------creating app ------------------


config = {"CACHE_TYPE": "RedisCache",
          "CACHE_REDIS_HOST": "localhost",
          "CACHE_REDIS_PORT": 7777,
          "CACHE_REDIS_URL": "redis://localhost:7777",
          "CACHE_DEFAULT_TIMEOUT": 1000}
app=Flask(__name__)
def create_app():
    app = Flask(__name__, template_folder="template")
    CORS(app)
    app.config['SECRET_KEY'] = 'ajay'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{data_base}'
    app.config.from_object(LocalDevelopementConfig)
    db.init_app(app)

    api = Api(app)
    cache=Cache(app)
    cache.init_app(app)
    app.config.from_mapping(config)
    print("config123",config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False