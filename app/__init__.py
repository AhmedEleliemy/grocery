from flask import Flask 


def create_app():
    """this a factory method that creates a flask app with the proper configuration"""
    app = Flask(__name__)
    return app