import app


requests_catalog = []
class User:
    """creates an instance of the class user"""

    def __init__(self, username, email,password,admin=False):
        self.username = username
        self.email = email
        self.password = password
        self.admin = admin
        
class Request:

    def __init__(self, title,description,category):
        self.title = title
        self.description = description
        self.category = category
    