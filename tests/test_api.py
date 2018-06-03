import unittest

import json

from app import app



class RequestsApiTestcase(unittest.TestCase):


    def setUp(self):

        app.config["Testing"] = True
        self.client = app.test_client()

        self.data =  {
                "request_title":"laptop",
                "request_description":"whitescreen",
                "request_category":"repair"
            }
        self.user_data = {
            "email":"example@gmail.com",
            "password":"12345",
            "username":"example"
        }
        
    def test_request_creation(self):
        """tests API can create a request"""
        create = self.client.post("/api/v1/users/requests", json=self.data,
        content_type =("application/json")
        )
        #from nose.tools import set_trace; set_trace()
        self.assertEqual(create.status_code,201)

    def test_add_empty_request_category(self):
            """Addition of empty category"""
            response = self.client.post("/api/v1/users/requests", 
                data=json.dumps(dict(request_title="office table", 
                request_description="The table stands"))
                ,content_type=("application/json"))

            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertEqual("category cannot be empty", response_msg['message']['request_category'])


    def test_get_returns_all_requests(self):
        """test all requests are returend"""
        #create resource
        create = self.client.post("/api/v1/users/requests", 
        data=json.dumps(self.data),
        content_type =("application/json")
        )
        self.assertEqual(create.status_code,201)
        #get resources created
        results = self.client.get("/api/v1/users/requests")
        response = results.data.decode('utf-8')
        #from nose.tools import set_trace; set_trace()
        self.assertIn("laptop", response)
        self.assertEqual(results.status_code,200)


    def test_get_method_returns_request_by_id(self):
        """Test a request can be succesfully retrieved"""

       #create resource
        create = self.client.post("/api/v1/users/requests", 
            data=json.dumps(self.data),
            content_type= ("application/json"))
        # access an item from resource created
        myrequest = self.client.get("/api/v1/users/requests/1")
        response = myrequest.data.decode("utf-8")
        
        self.assertIn("whitescreen", response)
        self.assertEqual(myrequest.status_code,200)
    
    def test_requests_can_be_edited(self):
        """test requets can be updated"""
        create = self.client.post("/api/v1/users/requests",
        data=json.dumps(self.data),
        content_type=("application/json")
        )
        # self.assertEqual(create.status_code,201)

        change = self.client.put("/api/v1/users/requests/1",
        data=json.dumps(dict(request_title ="kitchen",request_description="whitescreen",request_category="Repair")), content_type=("application/json"))
        results = self.client.get("/api/v1/users/requests/1")
        response_msg = json.loads(results.data.decode("UTF-8"))
        # from nose.tools import set_trace; set_trace()
        # self.assertEqual(results["request_title"], "kitchen")
        self.assertEqual("kitchen", response_msg["request_title"])


    def test_api_post_with_empty_request_title(self):
        """test post method returns error message when no title is submitted for a request"""
        create = self.client.post("/api/v1/users/requests",
         data=json.dumps(dict(request_description="toilet flush handles broken",
         request_category="repair")), 
        content_type="(application/json")
        response_msg = json.loads(create.data.decode("UTF-8"))
        self.assertEqual("title cannot be empty", response_msg["message"]['request_title'])


   


    def test_api_post_with_empty_request_description_field(self):
        """tests post method posts without the description field"""
        response = self.client.post("/api/v1/users/requests",
         data=json.dumps(dict(request_title="office mic",
         request_category="repair")),
        content_type=("application/json"))
        response_msg = json.loads(response.data.decode())
        self.assertEqual("description cannot be empty", response_msg["message"]["request_description"])


    def test_user_registration(self):
        """Test for user registration"""
        response = self.client.post("/api/v1/users",
        data=json.dumps(self.user_data),
        content_type =("application/json")
        )
        # from nose.tools import set_trace; set_trace()
        data = json.loads(response.data.decode())
        self.assertEqual(data["message"],"successfully registered")
        #from nose.tools import set_trace; set_trace()
        self.assertEqual(response.status_code,201)


    def test_registered_user_login(self):
        """Tests a registered user can successfully login"""
        #register the user
        create = self.client.post("/api/v1/users",
        data=json.dumps(dict(user_name="mel",user_email="mel@gmail",user_password="12345")),
        content_type =("application/json")
        )
        #login the user
        response= self.client.post("/api/v1/users/",
        data=json.dumps(dict(user_email="mel@gmail",user_password="12345")),
        content_type=("application/json"))
        response_msg = json.loads(response.data.decode())
        self.assertEqual(response_msg["message"],"successfully logged in")
        self.assertEqual(response.status_code,200)


    
        
        
        if __name__ == "__main__":
            unittest.main()