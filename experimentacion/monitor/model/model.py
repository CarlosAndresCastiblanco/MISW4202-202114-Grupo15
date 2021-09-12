from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
import enum

db = SQLAlchemy()

class TypeMonitor(enum.Enum):
    ON = 1
    OFF = 2

class Monitor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    autor = db.Column(db.String(128))
    data = db.Column(db.String(800))
    type = db.Column(db.Enum(TypeMonitor))
    date = db.Column(db.String(128))

class EnumADictionary(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {"llave": value.name, "valor": value.value}

class MonitorSchema(SQLAlchemyAutoSchema):
    type = EnumADictionary(attribute=("type"))
    class Meta:
         model = Monitor
         include_relationships = True
         load_instance = True