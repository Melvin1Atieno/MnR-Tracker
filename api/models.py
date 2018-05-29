
users={}
class User(object):
    """user model"""

    def __init__(self, email,username,password):
        self.email = email
        self.username = username
        self.password = password
        
    def addUser(self):
        users[self.email] = [self.username,self.password]
        return users
