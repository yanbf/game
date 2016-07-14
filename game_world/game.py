from flask import (
    Flask,
    Blueprint
)
from flask_sqlalchemy import SQLAlchemy
from views.user import user

# load config
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('default_settings.DevelopmentConfig')
app.config.from_pyfile('application.cfg', silent=True)

# initial db
db = SQLAlchemy(app)

# register blueprints
app.register_blueprint(user)

