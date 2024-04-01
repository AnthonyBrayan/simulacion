from flask import Flask

#Routes
from .routes import UsersRouter

app= Flask(__name__)

def init_app(config):
    app.config.from_object(config)

    app.register_blueprint(UsersRouter.main, url_prefix='/Users')

    return app

