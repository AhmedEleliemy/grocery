from flask import Flask 

from app.extensions import db, database_URI
from app.routes.apis import apis



def create_app():
    """this a factory method that creates a flask app with the proper configuration"""
    print(database_URI)
    app = Flask(__name__)
    app.register_blueprint(apis)
    return app
