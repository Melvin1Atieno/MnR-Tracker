import unittest

import os

import json



from api import create_app

from api import RequestListAPI
from api.models import User, Request



class RequestsApiTestcase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        
        self.client = self.app.test_client()

        self.request = {
            "request_title":"laptop", "request_description":"black screen","request_category":"Repair"
        }
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
        response = json.loads(results.data.decode("utf-8"))
        created_request = response[0]
        self.assertEqual(created_request["request_title"],"laptop")

    def test_get_method_returns_request_by_id(self):
        create = self.client.post("/api/v1/request", date=json.dumps(dict(request_title="laptop",request_description="whiteScreen",
        request_category="repair")))
        myrequest = self.client.get("/api/v1/request/0")
        response = json.loads(myrequest.data.decode("utf-8"))
        self.assertIn("whitescreen", response["request_description"])
        




    
if __name__ == "__main__":
    unittest.main()