from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

import enum

db = SQLAlchemy()

class Event(enum.Enum):
    REGISTRO = 1
    HISTORIACLINICA = 2

class Auditoria(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    date_register = db.Column(db.String(50))
    event = db.Column(db.Enum(Event))
    user = db.Column(db.String(50))
    is_correct = db.Column(db.Integer)


class EnumADiccionario(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {"llave": value.name, "valor": value.value}

class AuditoriaSchema(SQLAlchemyAutoSchema):
    event = EnumADiccionario(attribute=("event"))
    class Meta:
        model = Auditoria
        include_relationships = True
        load_instance = True