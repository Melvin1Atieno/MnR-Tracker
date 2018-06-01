# from ..app import request_catalog




class User:
    """user model"""
    count = 1#increase user id when user signs in
    def __init__(self, email, username,password):
        self.email = email
        self.username = username
        self.password = password
        self.id = User.count
        User.count +=1
          
        # user_list.append(user_details)
    
class Request(User):
    """Request model"""
    count = 1
    request_details = {}

    def __init__(self,request_title,request_description,request_category):
        self.request_title = request_title
        self.request_description = request_description
        self.request_category =request_category
        self.id = Request.count
        Request.count += 1
    
    def save_request(self):
        self.request_details[self.id] = [self.request_title,self.request_description, self.request_category]
        return self.request_details
    
