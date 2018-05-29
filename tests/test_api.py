import unittest

import os

import json



from api import create_app

from api.models import User

class TrackerApiTestcase(unittest.TestCase):

    def setUp(self):

        self.app = create_app(config_name="testing")

        self.client = UserApi("me@gmail","melvin","password")

        self.request = {"laptop":["Repair","black screen"]}


    def test_Api_can_get_all_requests(self):

        results = self.client().get("users/requests", data=self.requests)

        self.assertEqual(results.status_code, 200)

        self.assertIn("laptop", str(results.data))

    
if __name__ == "__main__":
    unittest.main()