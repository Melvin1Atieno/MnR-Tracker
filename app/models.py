import app
users_catalog = []

requests_catalog = []
class User:
    """creates an instance of the class user"""

    def __init__(self, username, email,password, admin):
        self.username = username
        self.email = email
        self.password = password
        self.user_details = {}
        self.admin = admin
        self.id = len(users_catalog)+1
        self.user_details[self.id] = [self.email, self.username, self.password,self.admin]

    def saveUser(self):
        users_catalog.append(self.user_details)
    
class Request:

    def __init__(self, title,description,category):
        self.title = title
        self.description = description
        self.category = category
        self.id = len(requests_catalog)+1
        self.request_details = {}
        self.request_details[self.id] = [self.title,self.description,self.category]
    
    def saveRequest(self):
        requests_catalog.append(self.request_details)