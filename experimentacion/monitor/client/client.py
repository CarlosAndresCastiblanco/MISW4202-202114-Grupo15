import json
import urllib3


class Client():

    def executeClient(self):
        http = urllib3.PoolManager()
        try:
            r = http.request(
                'GET',
                'http://127.0.0.1:5001/service',
                headers={'Content-Type': 'application/json'}
            )
            return json.loads(r.data.decode('utf-8'))
        except Exception:
            return None

