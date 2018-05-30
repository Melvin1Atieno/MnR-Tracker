
class User:
    """user model"""
    count = 0 #increase user id when user signs in
    def __init__(self, email, username,password):
        self.email = email
        self.username = username
        self.password = password
        self.id = User.count
        User.count +=1
    

class Request:
    """Request model"""
    count = 0 

    def __init__(self,request_title,request_description,request_category):
        self.request_title = request_title
        self.request_description = request_description
        self.request_category = request_category
        self.id = Request.count
        Request.count += 1


        
