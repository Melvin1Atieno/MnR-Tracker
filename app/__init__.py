from flask import Flask, request,jsonify,abort,make_response, json

from flask_restful import Api, Resource, reqparse

# from app import models

from app.models import Request

app = Flask(__name__)

api = Api(app)



parser = reqparse.RequestParser()
parser.add_argument('request_title', required=True, type=str, help="title cannot be empty")
parser.add_argument('request_description', required=True, type=str, help="description cannot be empty")
parser.add_argument('request_category', required=True, help="category cannot be empty")




request_catalog = []
users = {}


class Requests(Resource):


    def get(self):
        """get all requets"""
        return request_catalog,200



    def post(self):
        """create a request"""

        args = parser.parse_args()
        #get the count of stored requests
        count = len(request_catalog)
        request = {
            "request_id": count+1,
            "request_title": args['request_title'],
            "request_description": args['request_description'],
            "request_category": args['request_category'],
        }
        
        request_catalog.append(request)
        
        return request, 201



        
class SingleRequest(Resource):
    def get(self, id):
        """Get a single request"""
        for request_details in request_catalog:
            request_id = request_details.get("request_id")
            if request_id == id:
                return request_details,200
                
    def put(self,id):
        """update request details"""
        for request_details in request_catalog:
            for ids in request_details:
                if ids == id:
                    request_title = request.json.get("request_title")
                    request_description = request.json.get("request_description")
                    request_category = request.json.get("request_category")
                    updated_request = Request(request_title, request_description,request_categories)
                    request_catalog.remove(request_details)
                    request_catalog.append(updated_request)
                    return make_response(jsonify({"message":"updated"}),200)
                else:
                    abort(400)
                


api.add_resource(Requests, '/api/v1/users/requests', endpoint = "Requests")
api.add_resource(SingleRequest, "/api/v1/users/requests/<int:id>" )




