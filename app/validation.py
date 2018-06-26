from marshmallow import Schema, fields, validates, validates_schema, ValidationError
from app.models import User, Request


class UserSchema(Schema):
    """Validations for class User"""
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)



    @validates("username")
    def validate_fields(self,username):
        if " " in username:
            raise ValidationError ("Spaces not allowed")


    

    



class RequestSchema(Schema):
    """Validations for class Request"""
    title = fields.String(required=True) 
    description = fields.String(required=True)
    category = fields.String(required=True)