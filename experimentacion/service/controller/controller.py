from ..model import db, Service, ServiceSchema
from flask_restful import Resource

service_schema = ServiceSchema()

class ServiceInterface(Resource):

    def get(self):
        return [service_schema.dump(ca) for ca in Service.query.all()]