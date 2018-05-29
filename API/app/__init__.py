
from flask_api import FlaskAPI 


from instance.config import app_config

# loggedInUser = User()

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config)

    return app