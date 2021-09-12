import json
import time
from datetime import datetime

from flask import request
from urllib3.exceptions import NewConnectionError

from ..model import db, Monitor, MonitorSchema, TypeMonitor
from flask_restful import Resource
from ..client import Client
from sqlalchemy.exc import IntegrityError

monitor_schema = MonitorSchema()
client = Client()


class MonitorIterface(Resource):

    def post(self):
        steps = 1
        for i in range(request.json["times"]):

            now = datetime.now()
            date = now.strftime("%d/%m/%Y %H:%M:%S")
            data = client.executeClient()
            if data is not None:
                monitor = Monitor(autor=request.json["autor"], type=TypeMonitor.ON, date=date)
                monitor.data = json.dumps(data)
            else:
                monitor = Monitor(autor=request.json["autor"], type=TypeMonitor.OFF, date=date)
                monitor.data = json.dumps(data)
            db.session.add(monitor)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
            print(steps)
            steps = steps + 1
            time.sleep(3)

        return 'Ok', 200