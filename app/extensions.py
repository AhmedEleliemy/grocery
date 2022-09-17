from flask_sqlalchemy import SQLAlchemy 
import os

application_root_directory= os.path.abspath(os.path.dirname(__file__))+"/../"
database_file_name = "grocery.sqlite3"
database_URI = "sqlite:///"+application_root_directory+"/database/"+database_file_name
print(database_URI)
db = SQLAlchemy()