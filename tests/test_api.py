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
        
    def test_request_creation(self):
        """tests API can create a request"""
        create = self.client.post("/api/v1/users/requests", json=self.data,
        content_type =("application/json")
        )
        #from nose.tools import set_trace; set_trace()
        self.assertEqual(create.status_code,201)


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
        from nose.tools import set_trace; set_trace()
        self.assertIn("whitescreen", response)
        self.assertEqual(myrequest.status_code,200)
    
    # def test_requests_can_be_edited(self):
    #     """test requets can be updated"""
    #     create = self.client.post("/api/v1/users/requests/",
    #     data=json.dumps(self.data["request"]),
    #     content_type=("application/json")
    #     )
    #     self.assertEqual(create.status_code,201)

    #     change = self.client.put("/api/v1/users/requests/0/",
    #     data=json.dumps(dict(title ="kitchen"), content_type=("application/json")))
    #     results = self.client.get("/api/v1/requests/0")
    #     self.assertIn(results["title"], "kitchen")


    # def test_api_post_with_empty_request_title(self):
    #     """test post method returns error message when no title is submitted for a request"""
    #     create = self.client.post("/api/v1/users/requests", data=json.dumps(dict(request_title=" ",request_description="toilet flush handles broken",
    #     request_category="repair")), content_type="(application/json")
    #     response_msg = json.loads(create.data.decode("UTF-8"))
    #     self.assertIn("title cannot be empty", response_msg["message"])


    # def test_add_empty_request_category(self):
    #     """Addition of empty category"""
    #     response = self.client.post("/api/v1/users/requests", data=json.dumps(dict(request_title="office table", 
    #     request_description="The table stands",request_category="")),content_type=("application/json"))

    #     response_msg = json.loads(response.data.decode("UTF-8"))
    #     self.assertIn("category cannot be empty", response["message"])



    # def test_api_post_with_empty_request_description_field(self):
    #     """tests post method posts without the description field"""
    #     response = self.client.post("/api/v1/users/requests", data=json.dumps(dict(request_title="office mic",
    #     request_description="",request_category="repair")),content_type=("application/json"))
    #     response_msg = json.loads(response.data.decode())
    #     print(response)
    #     self.assertIn("description cannot be empty", response["message"])





        
        
        if __name__ == "__main__":
            unittest.main()