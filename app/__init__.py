from flask import Flask, request, jsonify, abort, make_response, json

import uuid

import datetime

import jwt

from functools import wraps

from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Request

from app.validation import UserSchema, RequestSchema

    
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
    
api = Api(app)

users_catalog = []
requests_catalog = []



# the decorator that works with the token
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # empty token
        token = None

        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]

        if not token:
            return{"message" : "Login is required "},401
        
        try:
            data = jwt.decode(token, "the secret secret ill use is here")
            # get the user to whom the token belongs to
            for users in users_catalog:
                if data["user_id"] in users:
                    current_user = users
        except:
            return{"message":"invalid token"}

        return f(current_user,*args,**kwargs)
        
    return decorated 


class UserRegistration(Resource):
    """ User registration resource"""

    @login_required
    def get(self):
        return users_catalog




    def post(self):
        """Create new user"""
        # get the post data
        post_data = request.get_json()

        # schema validation
        schema = UserSchema()
        results, errors = schema.load(post_data)
        if len(errors) > 0:
            return (errors),400

        # hash the password
        hashed_password = generate_password_hash(post_data.get("password"), method="sha256")
        # user_details = {}
        username = post_data.get("username")
        email = post_data.get("email")
        password = hashed_password



        
        # check if user already exists
        for user in users_catalog:
            if post_data.get("email") == user["email"]:
                return {"message":"Email already registered to an account"},400
            if post_data.get("username") == user["username"]:
                return {"message":"username already taken"},400
            if " "  in post_data.get("password"):
                return{"message":"Spaces not allowed"},400

        # make an instance of the User class
        new_user = User(username, email, hashed_password)

        # import pdb; pdb.set_trace()
        users_catalog.append({"username":new_user.username, "email":new_user.email, "password":new_user.password})
        return {"message":"New user successfully registered"},201


class UserLogin(Resource):
    """login a user"""

    def post(self):
        # get the authorization information 
        post_data = request.get_json()
        

        # make sure the authorization info is complete
        
        if not post_data or not post_data.get("username") or not post_data.get("password"):
           return make_response("could not verify", 401)

        # get the user
        for user in users_catalog:
            # print(user)
            if post_data.get("username") == user["username"]:
                # compare stored password with password entered
                if check_password_hash(user["password"], post_data.get("password")):
                    token = jwt.encode({"user_email":user["email"], "exp":datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},"the secret secret ill use is here")
                    return {"token": token.decode("UTF-8"),"message":"successfully logged in","status_code":200}
                # import pdb; pdb.set_trace()
                return{"message":"incorrect password"},401
        return{"message":"User does not exist"},401
    
# class Requests(Resource):
#     """get rewquest and post a request"""

#     @login_required
#     def get(self, current_user):
#         return requests_catalog

#     @login_required
#     def post(self, current_user):
#         post_data = request.get_json()

#         title = post_data.get("title")
#         description = post_data.get("description")
#         category = post_data.get("category")

#         myrequest = Request(title, description,category)

#         myrequest.saveRequest()

#         return{"message":"request successfully created"}


# class singleRequest(Resource):

#     @login_required
#     def get(self,current_user, request_id):
#         """get a single request"""
#         user_id = current_user.user_id
#         # check if user is admin or n

#         if request_id > len(requests_catalog):
#             return {"message":"the request does not exist"}
#         for requests in requests_catalog:
#             if request_id == ids:
#                 return requests

#     @login_required
#     def put(self,current_user, request_id):
#         """Edit a single request"""
#         if request_id > len(requests_catalog):
#             return {"message":"the request does not exist"}
#         for request_details in requests_catalog:
#             if request_id == ids:
#                 post_data = request.get_json()
#                 new_title = post_data.get("title")
#                 new_description = post_data.get("description")
#                 new_category =post_data.get("category")
#                 request_details[request_id] = [new_title, new_description, new_category]
#                 return {"message":"request successfully updated"}


#     @login_required
#     def delete(self,current_user, request_id):
#         """Delete a request by id"""
#         if request_id > len(requests_catalog):
#             return {"message":"the request does not exist"}
#         for request_details in requests_catalog:
#             if request_id == ids:
#                 requests_catalog.remove(request_details)
#                 return {"message":"request successfully deleted"}






api.add_resource(UserLogin, "/api/v1/users/auth/login", endpoint="login")
api.add_resource(UserRegistration, "/api/v1/users/registration", endpoint="users")
# api.add_resource(Requests,"/api/v1/requests", endpoint="requests")
# api.add_resource(singleRequest,"/api/v1/requests/<int:request_id>", endpoint="singleRequest")



