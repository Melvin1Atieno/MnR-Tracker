import os

from instance.config import app_config

from app import app

# config_name = os.getenv("APP_SETTINGS")

# app = create_app(config_name)

if __name__ == "__main__":
    app.run(debug=True)