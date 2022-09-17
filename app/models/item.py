from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields, validate
from app.extensions import db

class Item(db.Model):
    __tablename__ = "items"
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    
    def __init__(self,name, description, quantity, price):
        self.name=name
        self.quantity=quantity
        self.description=description 
        self.price = price

    def __repr__(self) -> str:
        return "{"+"'id':{}, 'name':'{}', 'description':'{}', 'price':{}, 'quantity':{}".format(self.id, 
        self.name, self.description, self.price, self.quantity)+"}"
        

class ItemSchema(SQLAlchemySchema):
    class Meta:
        model = Item
        load_instance = True    
    id = auto_field()
    name= fields.Str(required=True, validate=validate.Length(min=1))
    description = fields.Str(required=True, validate=validate.Length(min=1))
    price = fields.Float(required=True,validate=[validate.Range(min=0.0, error="Value must be greater than 0.0")])
    quantity = fields.Int(required=True, validate=[validate.Range(min=0, error="Value must be greater than 0")])