from flask import Flask
from flask_cors import CORS
#Routes
from src.routes import UsersRouter
from src.routes import AuthRouter

app= Flask(__name__)

CORS(app,resources={"*":{"origins": "http://localhost:5173"}})

def init_app(config):
    app.config.from_object(config)

    app.register_blueprint(UsersRouter.main, url_prefix='/Users')
    app.register_blueprint(AuthRouter.main, url_prefix='/Login')

    return app

