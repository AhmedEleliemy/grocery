from flask import Flask 
from app.extensions import db, database_URI

def create_app():
    """this a factory method that creates a flask app with the proper configuration"""
    print(database_URI)
    app = Flask(__name__)
    return app
