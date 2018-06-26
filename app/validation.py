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


    # @validates("password")
    # def validate_fields(self,password):
    #     if " " in password:
    #         raise ValidationError("Spaces not allowed")

    

    



class RequestSchema(Schema):
    """Validations for class Request"""
    title = fields.String() 
    description = fields.String()
    category = fields.String()