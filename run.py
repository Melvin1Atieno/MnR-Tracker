import os

from instance.config import app_config

from app import app

def create_app(config_filename):
    app = Flask(__name__)

    app_config.from_object(config_filename)

    api




if __name__ == "__main__":
    app.run(debug=True)