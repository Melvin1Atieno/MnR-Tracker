from flask import Flask, request,jsonify,abort,make_response, json

import uuid


import datetime

import jwt

from functools import wraps

from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Request, users_catalog,requests_catalog

    
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
    
api = Api(app)




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

        # hash the password
        hashed_password = generate_password_hash(post_data.get("password"), method="sha256")

        username = post_data.get("username")
        email   = post_data.get("email")
        password = hashed_password

        if username == " ":
            return {"message":"Username field cannot be empty"},401
        if not username:
            return {"message":"Username must be provided"},401
        if not email :
            return {"message":"Email must be provided"},401
        if email == " ":
            return {"message":"Email field cannot be empty"},401
        if not post_data.get("password"):
            return {"message":"password must be provided"},401
        if post_data["password"] == " ":
            return {"message":"password field cannot be empty"},401


        # make the user an instance of the user class
        new_user = User(username, password,email, admin=False)

        

        # check if user already exists

        # import pdb; pdb.set_trace()
        if len(users_catalog) > 0:
            for users in users_catalog:
                for ids, details in users.items():
                    if email in details:
                        return {"message":"Email already registered to an account"}
                    if username in details:
                        return {"message":"username already taken"}
        new_user.saveUser()
        return {"message":"New user successfully registered"},201



class UserLogin(Resource):
    """login a user"""

    def post(self):
        # get the authorization information 
        auth = request.authorization

        # make sure the authorization info is complete
        # import pdb; pdb.set_trace()
        if not auth or not auth.username or not auth.password:
            return make_response("could not verify", 401, {"www-authenticate":"Basic realm ='Login required'"})

        # get the user
        for users in users_catalog:
            for ids, details in users.items():
                if auth.username not in details:
                    return{"message":"User does not exist"}
                    # compare stored password with password entered
                if check_password_hash(users[ids][0], auth.password):
                    token = jwt.encode({"user_id":ids, "exp":datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},"the secret secret ill use is here")
                    return {"token": token.decode("UTF-8"),"message":"successfully logged in"},200
                return {"message":"login required"}
    
class Requests(Resource):
    """get rewquest and post a request"""

    @login_required
    def get(self, current_user):
        return requests_catalog

    @login_required
    def post(self, current_user):
        post_data = request.get_json()

        title = post_data.get("title")
        description = post_data.get("description")
        category = post_data.get("category")

        myrequest = Request(title, description,category)

        myrequest.saveRequest()

        return{"message":"request successfully created"}


class singleRequest(Resource):

    @login_required
    def get(self,current_user, request_id):
        """get a single request"""
        if request_id > len(requests_catalog):
            return {"message":"the request does not exist"}
        for requests in requests_catalog:
            for ids in requests:
                if request_id == ids:
                    return requests

    @login_required
    def put(self,current_user, request_id):
        """Edit a single request"""
        if request_id > len(requests_catalog):
            return {"message":"the request does not exist"}
        for request_details in requests_catalog:
            for ids in request_details:
                if request_id == ids:
                    post_data = request.get_json()
                    new_title = post_data.get("title")
                    new_description = post_data.get("description")
                    new_category =post_data.get("category")
                    request_details[request_id] = [new_title, new_description, new_category]
                    return {"message":"request successfully updated"}


    @login_required
    def delete(self,current_user, request_id):
        """Delete a request by id"""
        if request_id > len(requests_catalog):
            return {"message":"the request does not exist"}
        for request_details in requests_catalog:
            for ids in request_details:
                if request_id == ids:
                    requests_catalog.remove(request_details)
                    return {"message":"request successfully deleted"}






api.add_resource(UserLogin, "/api/v1/users/auth/login", endpoint="login")
api.add_resource(UserRegistration, "/api/v1/users/registration", endpoint="users")
api.add_resource(Requests,"/api/v1/requests", endpoint="requests")
api.add_resource(singleRequest,"/api/v1/requests/<int:request_id>", endpoint="singleRequest")



