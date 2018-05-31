import unittest

import os

import json



from api import create_app

from api import RequestListAPI
# from api.models import User, Request



class RequestsApiTestcase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        
        self.client = self.app.test_client()

    def test_request_creation(self):
        """tests API can create a request"""
        create = self.client.post("/api/v1/requests", data= json.dumps(dict(request_title="laptop",request_description="whiteScreen",
        request_category="repair")), content_type ="application/json")
        response = json.loads(create.data.decode())
        self.assertIn("Request successfully created", response["message"])


    def test_get_returns_all_requests(self):
        """test all requests are returend"""
        create = self.client.post("/api/v1/requests", data=json.dumps(dict(request_title="laptop",request_description="whiteScreen",
         request_category="repair")),content_type ="application/json")
        results = self.client.get("/api/v1/requests/")
        response = json.loads(results.data.decode())
        created_request = response[0]
        self.assertEqual(created_request["request_title"],"laptop")

    def test_get_method_returns_request_by_id(self):
        create = self.client.post("/api/v1/requests", data=json.dumps(dict(request_title="laptop",request_description="whiteScreen",
        request_category="repair")), content_type="application/json")
        myrequest = self.client.get("/api/v1/requests/0")
        response = json.loads(myrequest.data.decode())
        self.assertIn("whitescreen", response["request_description"])

    
    def test_requests_can_be_edited(self):
        """test requets can be edited"""
        response = self.client.post("/api/v1/requests/",
        data=json.dumps(dict(request_title="windows", request_description="dirty", request_category="maintenance")),content_type="application/json")
        change = self.client.put("/api/v1/requests/0", data=json.dumps(dict(request_title="kitchen", 
        request_description="dirty",request_category="maintenance")), content_type="application/json")
        results = self.client.get("/api/v1/requests/0")
        self.assertIn(results["request_title"], "kitchen")


    def test_api_post_with_empty_request_title(self):
        """test post method returns error message when no title is submitted for a request""""
        response= self.client.post("/api/v1/requests", data=json.dumps(dict(request_title="",request_description="toilet flush handles broken",
        request_category="repair")), content_type="application/json")
         response_msg = json.loads(response.data.decode("UTF-8"))
         self.assertIn("request_title required", response_msg["message"])


    def test_add_empty_request_category(self):
        """Addition of empty category"""
        response = self.client.post("/api/v1/requests", data=json.dumps(dict(request_title="office table", 
        request_description="The table stands",request_category="")),content_type="application/json")
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Category is required", response_msg["message"])



    def test_api_post_with_empty_request_description_field(self):
        """tests post method posts without the description field"""
        response = self.client.post("/api/v1/business", data=json.dumps(dict(request_title="office mic",
        request_description=" ",request_category="repair"))content_type="application/json")
        response_msg = json.loads(response.dat.decode())
        self.assertIn("Description is required", response_msg["message"])





        
        
        if __name__ == "__main__":
            unittest.main()