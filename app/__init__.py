from flask import Flask, request,jsonify,json,abort,make_response

from flask_restful import Api, Resource, reqparse

# from app import models

from app.models import Request

app = Flask(__name__)

api = Api(app)



request1 = Request("laptop repair","Broken screen/keyboard","Repair")
request2 = Request("window repair", "shattered glass", "maintenance")



request_catalog = []
users = {}


class Requests(Resource):


    def get(self):
        """get all requets"""
        return jsonify({"request_catalog":request_catalog},200)


    def post(self):
        """create a request"""
        # if not request.json or  "request_title" not in request.json or "request_description" not in request.json or "request_category" not in request.json:
        #     abort(404)
        request_title = request.json.get("request_title")
        if request_title == "":
            return make_response(jsonify({"error": "description cannot be empty"}),400)
        request_description = request.json.get("request_description")
        if request_description == "":
            return make_response(jsonify({"error": "description cannot be empty"}),400)
        request_category = request.json.get("request_title")
        if request_category == "":
            return make_response(jsonify({"error": "description cannot be empty"}),400)
        request = Request(request_title,request_description,request_category)
        request_catalog.append(request)

        return jsonify({"request":request}),201




        
class SingleRequest(Resource):
    def get(self, id):

        """Get a single request"""
        for request_details in request_catalog:
            for ids in request_details:
                if ids == id:
                    return jsonify({"request_details":request_details})
                abort(404)
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
                    return make_response(jsonify({"message":"updated"})200)
                else:
                    abort(400)
                


api.add_resource(Requests, '/api/v1/users/requests', endpoint = "Request")
api.add_resource(SingleRequest, "/api/v1/users/requests/<int:id>",endpoint ="Requests" )





