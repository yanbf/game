from app import app
from views.user import user

# register blueprints
app.register_blueprint(user)

