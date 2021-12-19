#!/usr/bin/python3 

from flask import Flask
from flask_login import LoginManager
from .models import UserBase

print(UserBase.sessions)

def create_app():
    app=Flask(__name__)
    app.secret_key='slkdncskjdfbvjdhfbvjdsbc'

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .file import file as file_blueprint
    app.register_blueprint(file_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
      
       return UserBase.sessions[user_id]
       #return UserBase.logins['user']

    return app
