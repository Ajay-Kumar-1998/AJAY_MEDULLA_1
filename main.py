from flask import Flask
from flask_login import LoginManager, login_manager
from flask_restful import Api
from application.config import LocalDevelopementConfig
from application.db_init import db
from os import path







def create_app():
    app = Flask(__name__, template_folder="template")
    app.config['SECRET_KEY'] = 'ajay'

    app.config.from_object(LocalDevelopementConfig)
    db.init_app(app)

    api = Api(app)
    app.app_context().push()

#     app.config.from_mapping(config)
#     print("config123",config)
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#-----------------adding api resources----------------



#------------- creating view blue prints--------------
#     from application.controllers import views
#     app.register_blueprint(views, url_prefix="/")




#-----------------login manager--------------
#     login_manager = LoginManager()
#     login_manager.login_view = "views.login"
#     login_manager.init_app(app)
#     @login_manager.user_loader
#     def load_user(id):
#         return User.query.get(int(id))

#---------------- returnind app, api----------------
    return  app, api

from application.controllers import *




if __name__ == "__main__":
     app,api=create_app()
     app.run(debug=True, host="0.0.0.0", port=7000)