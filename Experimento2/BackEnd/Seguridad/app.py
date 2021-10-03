from jwtManager import create_app
from flask_restful import Api
from .model import db
from .controller import ControllerLogIn, ControllerService
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)

api = Api(app)
api.add_resource(ControllerLogIn, '/login')
api.add_resource(ControllerService, '/service')
jwt = JWTManager(app)