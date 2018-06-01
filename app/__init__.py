from flask import Flask, request,jsonify,json

from flask_restful import Api, Resource, reqparse

# from app import models

from app.models import Request

app = Flask(__name__)

api = Api(app)



request1 = Request("laptop repair","Broken screen/keyboard","Repair")
request2 = Request("window repair", "shattered glass", "maintenance")



request_catalog = []
users = {}
request_catalog.append(request2.save_request())
request_catalog.append(request1.save_request())

parser = reqparse.RequestParser()
parser.add_argument('request_title', required=True, type=str, help="title cannot be empty")
parser.add_argument('request_description', required=True, type=str, help="description cannot be empty")
parser.add_argument('request_category', required=True, type=str, help="category cannot be empty")


class Requests(Resource):


    def get(self):
        """get all requets"""
        return {"request_catalog":request_catalog},200


    def post(self):
        """create a request"""
        args = parser.parse_args()
        request = {
            "request_title":args["request_title"],
            "request_description":args["request_description"],
            "request_category":args["request_category"]
        }
        request = Request("request_title","request_description","request_category")

        request_catalog.append(request)

        return{"request":request}, 201
        
class SingleRequest(Resource):
    """"""


api.add_resource(Requests, '/api/v1/users/requests', endpoint = "Request")
api.add_resource(SingleRequest, "/api/v1/users/requests/<int:id>",endpoint ="Requests" )





