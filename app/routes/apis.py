import markdown
from app.extensions import application_root_directory, db
from flask import Blueprint, jsonify
from app.routes import apis
from app.models.item import Item, ItemSchema


#defining apis as blueprint and register it
apis=Blueprint('apis', __name__)

#for data serialization and validation
items_schema= ItemSchema(many=True)

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