from flask import Flask
from service.model import Service, ServiceSchema

def create_app(config_name):
    app = Flask(__name__)  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///service.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app