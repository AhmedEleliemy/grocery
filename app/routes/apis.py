import markdown
from app.extensions import application_root_directory, db
from flask import Blueprint, jsonify, request
from app.routes import apis
from app.models.item import Item, ItemSchema
from sqlalchemy.exc import IntegrityError
from distutils.log import error
from marshmallow import ValidationError


#defining apis as blueprint and register it
apis=Blueprint('apis', __name__)

#for data serialization and validation
items_schema= ItemSchema(many=True)
item_schema= ItemSchema(many=False)

#default will render the readme file
@apis.route('/')
def index():
    #application_root_directory= os.path.abspath(os.path.dirname(__file__))
    with open(application_root_directory+"/README.md", 'r') as home_page:
        # read content of the file
        content=home_page.read()
        #convert markdown into html and return it
        return markdown.markdown(content)


#this end-point is to list  all items from the database 
@apis.route('/items', methods=['GET'])
def get_all_grocery_items():
    #get all grocery items for the database with the ORM object
    items=Item.query.all()
    result = items_schema.dump(items)
    return jsonify(result),200


#this end-point is to create a  new item in the database 
@apis.route('/items', methods=['POST'])
def add_grocery_item():
    # check if the posted json object has proper formate
    json_object=request.json
    error={}
    result={}
    try:
        #validate the json object to ensure it has the same exact required fields and proper values
        print(request)
        print(json_object)
        posted_item=item_schema.load(json_object, session=db.session)
        #add the posted grocery item to the database
        db.session.add(posted_item)
        #commit the transaction
        db.session.commit()
        # catch the id of the newly added grocery item 
        result['id']= posted_item.id
        #return the id of the newly added grocery item and a successfully created status code
        return  jsonify(result), 201
    except IntegrityError as err:
        # catch IntegrityError if the posted item already exist
        error['message']= str(err)
        return jsonify(error), 409 
    except ValidationError as err:
        # catch ValidationError if the posted item is not valid
        error['message']= str(err)
        return jsonify(error), 400  
