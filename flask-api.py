# Refer: https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

payload = {'name': 'Maruti'}

class Payload(Resource):
    def get(self):
        print('Received!')
        return payload

class Set(Resource):
    def get(self, parameter, value):
        print(parameter)
        return value


api.add_resource(Payload, '/api/payload')

api.add_resource(Set, '/set/<parameter>/<value>')


if __name__ == '__main__':
    app.run(debug=True)