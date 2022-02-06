from flask import Flask

def create_app():
    app = Flask(__name__)    
    SECRET_KEY = 'Njoro'

    from .main.views import views
    from .auth.views import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app