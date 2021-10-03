from flask_restful import Resource
from ..models import db, Auditoria,AuditoriaSchema
from flask import request

auditoria = AuditoriaSchema()

class VistaAuditoria(Resource):
    def post(self):
        event = Auditoria(date_register=request.json['date_register'],event=request.json['event'],\
            user=request.json['user'],is_correct=request.json['is_correct'])
        db.session.add(event)
        db.session.commit()
        return auditoria.dump(event)
