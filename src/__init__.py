from flask import Flask

#Routes
from src.routes import UsersRouter
from src.routes import AuthRouter

app= Flask(__name__)

def init_app(config):
    app.config.from_object(config)

    app.register_blueprint(UsersRouter.main, url_prefix='/Users')
    app.register_blueprint(AuthRouter.main, url_prefix='/Login')



    return app

