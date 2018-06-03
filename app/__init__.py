from flask import Flask, request,jsonify,abort,make_response, json
import jwt

from jwt import decode, encode


from flask_restful import Api, Resource, reqparse

from app.models import encode_auth_token,decode_auth_token

from app.models import Request, User
import datetime

app = Flask(__name__)
    
api = Api(app)


    



parser = reqparse.RequestParser()
parser.add_argument('request_title', required=True, type=str, help="title cannot be empty")
parser.add_argument('request_description', required=True, type=str, help="description cannot be empty")
parser.add_argument('request_category', required=True, help="category cannot be empty")



user_details = {}
request_catalog = []
users = {}
# set default login status to False
logged_in = False


class UsersRegistration(Resource):
    """ User registration resource"""


    def post(self):
        """Create new user"""
        # get the post data
        post_data = request.get_json()


        #checks if username already exists
        user_username = post_data.get("user_username")
        user_email = post_data.get("user_email")
        if user_username in users:
            return {"message":"username already exists"}, 400
        elif user_email in users:
            return {"message":"email registered under an existing account"},400
        else:
            # generate an id for the user 
            count = len(users)
             # add user to dict  of users
            user_details= [
                post_data.get("user_username"),post_data.get("user_email"),post_data.get("user_password")
                ]
            user_id = count + 1
            users[user_email] = user_details
            return {"message":"successfully registered",
                    "message":"login link below",
                    "url":"http://127.0.0.1:5000/api/v1/users/"},201
    
class UserLogin(Resource):
    """User login resource"""

    def post(self):
        """login an existing user"""

        #get post data
        post_data = request.get_json()


        #verify that user exists
        user_email = post_data.get("user_email")

        for users_details in users:
            # import pdb; pdb.set_trace()       
            if user_email in users_details:
                single_user_details = users[user_email]
                user_password = single_user_details[2]
                entered_password = post_data.get("user_password")
                if user_password == entered_password:
                    logged_in = True
                    return {"message":"successfully logged in",
                             "url" : "http://127.0.0.1:5000/api/v1/users/requests",
                             },200
                logged_in = False
                return {"message":"Password email combination incoreect try again"}, 401
            return {"message":"email does not exist"}, 400
        







        

class RequestsAPI(Resource):
    """Requests resource"""


    def get(self):
        """get all requets"""
        if logged_in == False:
            return {"message":"You have to login first",
                    "url":"http://127.0.0.1:5000/api/v1/users/"}
        return request_catalog,200



    def post(self):
        """create a request"""

        if logged_in == False:
            return {"message":"You have to login first to access resource",
                    "url":"http://127.0.0.1:5000/api/v1/users/"}
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


        
class SingleRequestAPI(Resource):
    def get(self, id):
        """Get a single request"""
        if logged_in == False:
            return{"message":"You have to be logged in"}
        for request_details in request_catalog:
            request_id = request_details.get("request_id")
            if request_id == id:
                return request_details,200

    def put(self,id):
        """update request details"""
        if logged_in == False:
            return {"message":"You have to login first to access resource",
                     "url":"http://127.0.0.1:5000/api/v1/users/"}
        for request_details in request_catalog:
            request_id = request_details.get("request_id")
            if request_id == id:
                request_title = request.json.get("request_title")
                request_description = request.json.get("request_description")
                request_category = request.json.get("request_category")
                
                
                updated_request = {
                    "request_id": request_id,
                    "request_title": request_title,
                    "request_description": request_description,
                    "request_category": request_category
                    
                    }
    
                request_catalog.remove(request_details)
                request_catalog.append(updated_request)
                
                response = jsonify({"message":"request details updated"})
                response.status_code = 200
                
                return response
            else:
                abort(404)
                
                
   


api.add_resource(RequestsAPI, '/api/v1/users/requests', endpoint = "requests")
api.add_resource(SingleRequestAPI, "/api/v1/users/requests/<int:id>", endpoint="request" )
api.add_resource(UsersRegistration, "/api/v1/users/registration", endpoint="users_registration")
api.add_resource(UserLogin,"/api/v1/users/", endpoint="users_login")



