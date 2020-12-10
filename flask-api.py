# Refer: https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

payload = {
    'connection': False,
    'pstatus': [ 1, 2],
    'pLHS_data': [],
    'pLHS_processed': [],
    'pRHS_data': [],
    'pRHS_processed': [],
    'mLHS_data': [],
    'mLHS_processed': [],
    'mRHS_data': [],
    'mRHS_processed': [],
    'eLHS_data': [],
    'eLHS_processed': [],
    'eRHS_data': [],
    'eRHS_processed': [],
    'avg': [],
    'stats': []
}

VART = 10

class Payload(Resource):
    def get(self):
        print('Received!')
        return VART

class Set(Resource):
    def get(self, parameter, value):
        global VART
        if parameter == "pressure":
            VART = 100
            return parameter+" set to "+value
        elif parameter == "machine":
            return value
        else:
            return "Invalid Command"

api.add_resource(Payload, '/api/payload')

api.add_resource(Set, '/set/<parameter>/<value>')

if __name__ == '__main__':
    app.run(debug=True)