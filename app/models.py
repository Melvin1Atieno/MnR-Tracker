# from ..app import request_catalog

request_catalog=[]
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

    def __init__(self,request_title,request_description,request_category):
        self.request_title = request_title
        self.request_description = request_description
        self.request_category = request_category
        self.id = Request.count
        Request.count += 1
    
    def to_dict(self):
        request_details = {
            "id":self.id,
            "title":self.request_title,
            "description":self.request_description,
            "category": self.request_category
        }
        request_catalog.append(request_details)
        return request_details

    def from_dict(self, request_details):
        for fields in ["title","description","category"]:
            if field in data:
                setattr(self,fields,request_details[field])
        
    def returns_catalog(self):
        return request_catalog

        
