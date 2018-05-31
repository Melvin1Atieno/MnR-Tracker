from flask import Flask

from flask_restful import Api, Resource, reqparse, fields, marshal


from instance.config import app_config

# loggedInUser = User()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config)

    api = Api(app)
    return app
    
    REQUESTS = []



@app.route("/api/v1/requests/", methods=["GET"])
def get_all_requests()
"""Returns a list of all requests """
get_request = [requests for requests in REQUESTS]
if not get_request:
    return jsonify ({"message":"Requests not found"}), 409
found_request = [{"request_title":requests.request_title, "request_description":requests.request_description,
"category":request.request_category,"id":requests.id} for requests in REQUESTS]
return jsonify(found_request),200
