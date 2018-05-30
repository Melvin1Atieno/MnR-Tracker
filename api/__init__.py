from flask import Flask

from flask_restful import Api, Resource, reqparse


from instance.config import app_config

# loggedInUser = User()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config)

    api = Api(app)
    return app


class RequestListAPI(Resource):
    def get(self):
        pass
    
    def post(self):
        pass

class RequestAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass


# api.add_resource("/MnRtracker/api/v1.0/users/requests", endpoint ="tasks")