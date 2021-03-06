from monitor import create_app
from flask_restful import Api
from .model import db
from .controller import MonitorIterface
from flask_cors import CORS, cross_origin

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)

api = Api(app)
api.add_resource(MonitorIterface, '/monitor')