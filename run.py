import os

from instance.config import app_config

from app import app




if __name__ == "__main__":
    app.run(debug=True)