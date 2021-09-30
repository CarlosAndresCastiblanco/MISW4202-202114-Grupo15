import json
import urllib3


class Client():

    def executeClient(self,user):
        http = urllib3.PoolManager()
        try:
            r = http.request(
                'POST',
                'http://127.0.0.1:5001/register',
                data=json.dumps(dict(
                    nombre=user.nombre,
                    contrasena=user.contrasena
                )),
                headers={'Content-Type': 'application/json'}
            )
            return json.loads(r.data.decode('utf-8'))
        except Exception:
            return None

