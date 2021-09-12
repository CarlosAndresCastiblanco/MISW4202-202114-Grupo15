from service import create_app
from flask_restful import Api
from .model import db
from .controller import ServiceInterface
from flask_cors import CORS, cross_origin
from .model import Service

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)

api = Api(app)

newServiceOne = Service(data="data_test", time=120)
db.session.add(newServiceOne)
newServiceTwo = Service(data="data_test", time=121)
db.session.add(newServiceTwo)
newServiceThree = Service(data="data_test", time=122)
db.session.add(newServiceThree)
newServiceFour = Service(data="data_test", time=123)
db.session.add(newServiceFour)
newServiceFive = Service(data="data_test", time=124)
db.session.add(newServiceFive)
newServiceSix = Service(data="data_test", time=125)
db.session.add(newServiceSix)
newServiceSeven = Service(data="data_test", time=126)
db.session.add(newServiceSeven)
db.session.commit()

api.add_resource(ServiceInterface, '/service')