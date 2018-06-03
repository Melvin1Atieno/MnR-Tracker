# from ..app import request_catalog
import jwt

import datetime

import app

from instance.config import Config


def encode_auth_token( user_id):
     """Generates the Auth Token :return: string"""
     try:
         payload = {
             'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),#expiration date of the Token
             'iat': datetime.datetime.utcnow(),#the time the token is generated
             'sub': user_id #the subject of the token(the user whom it identifies)
             }
         return jwt.encode(
             payload,
             app.config.get('SECRET_KEY'),
             algorithm='HS256')
     except Exception as e:
         return e
def decode_auth_token(auth_token):
    """ Decodes the auth token
        :param auth_token: :return: integer|string"""
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
class User:
    """user model"""
    #increase user id when user signs in
    def __init__(self,user_id):
        self.user_id = user_id
        

    
class Request(User):
    """Request model"""
    request_details = {}
    request_catalog = []

    def __init__(self,request_title,request_description,request_category):
        self.request_title = request_title
        self.request_description = request_description
        self.request_category =request_category
        self.request_id = request_id

    def save_request(self):
        self.request_details[self.id] = [self.request_id, self.request_title, 
                                        self.request_description,self.request_category]
        request_catalog.append(request)
    
