from flask import Flask

# load config
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('default_settings.Config')
app.config.from_pyfile('application.cfg', silent=True)

# register blueprints
from views.user import user
app.register_blueprint(user)

