from flask import Flask,jsonify, request, json

from flask_restful import Api, Resource, reqparse, fields, marshal


from instance.config import app_config

# loggedInUser = User()

# def create_app(config_name):
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config)
api = Api(app)
# return api
REQUESTS = []




@app.route("/api/v1/requests/", methods=["GET"])
def get_all_requests():
    """Returns a list of all requests """
    get_request = [requests for requests in REQUESTS]
    if not get_request:
        return jsonify ({"message":"Requests not found"}), 409
        found_request = [{"request_title":requests.request_title, "request_description":requests.request_description,
        "category":request.request_category,"id":requests.id} for requests in REQUESTS]
        return jsonify(found_request),200




@app.route('/api/v1/requests', methods=['POST'])
def create_a_request():
    """Users can create new requests"""
    new_request = request.get_json()
    request_title = new_request.get('request_title')
    request_description  = new_request.get('request_description')
    request_category = new_request.get('category')
    dict_data = {'request_title': request_title, 'request_description': request_description,
    'request_category': request_category}

    existing_requests = [req.requests for req in REQUESTS]

    if request_title  in existing_requests:
        return jsonify({'message': 'request already exists'}), 409
 
    new_request = Request(request_title, request_description,request_category)
    REQUESTS.append(new_request)
    return jsonify({'message': 'You have successfully made your request'}), 201