from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()


def post(self):
    parser.add_argument('quote', type=str)
    args = parser.parse_args()

    return {
        'status': True,
        'quote': '{} added. Good'.format(args['quote'])
    }

