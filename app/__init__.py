from flask import Flask, request,jsonify,json

from flask_restful import Api, Resource

# from app import models

from app.models import Request

app = Flask(__name__)

api = Api(app)



request1 = Request("laptop repair","Broken screen/keyboard","Repair")
request2 = Request("window repair", "shattered glass", "maintenance")
request1.to_dict()


class Requests(Resource):
    def get(self):
        """get all requets"""
        return jsonify({"request":request1}),200


    def post(self):
        """create a request"""
        if not request.json or "request_title" not in request.json or "request_description" not in request.json or "request_category" not in request.json:
            abort(400)
           
        request_title = request.json.get("request_title")

        request_description = request.json.get("request_description")

        request_category = request.json.get("request_category")

        if request_title == " ":
            return jsonify({"response" :"request title is required"})
        if request_description == " ":
            return jsonify({"response":"request description is required"})
        if request_category == " ":
            return jsonify({"response":"request category is required"})
        new_request = Request(request_title,request_description,request_category)
        new_request.add_request()
        return jsonify({"request_details":request_details}), 201
class SingleRequest(Resource):
    """"""


api.add_resource(Requests, '/api/v1/requests', endpoint = "Request")
api.add_resource(SingleRequest, "/api/v1/requests/<int:id>",endpoint ="Requests" )





