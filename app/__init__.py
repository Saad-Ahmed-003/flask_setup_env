from flask import Flask
from .config import get_config

def create_app():
    app = Flask(__name__)

    config_name = 'development'  # Change this based on the desired environment
    app.config.from_object(get_config(config_name))

    # Initialize extensions or blueprints here, if needed

    return app
