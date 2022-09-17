from flask import Flask 

from app.extensions import db, database_URI
from app.routes.apis import apis



def create_app():
    """this a factory method that creates a flask app with the proper configuration"""
    print(database_URI)
    #creation of the flask app
    app = Flask(__name__)
    #register apis blueprint
    app.register_blueprint(apis)

    #configure the data base
    app.config['SQLALCHEMY_DATABASE_URI'] = database_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
