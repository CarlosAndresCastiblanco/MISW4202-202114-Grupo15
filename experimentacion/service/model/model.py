from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Service(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(128))
    time = db.Column(db.Integer)

class ServiceSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Service
         include_relationships = True
         load_instance = True