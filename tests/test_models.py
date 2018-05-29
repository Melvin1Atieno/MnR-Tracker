
import unittest

from api.models  import User

class TestUserClass(unittest.TestCase):

    def setUp(self):
        self.myuser= User("me@gmail","melvin","password")

    def test_adduser_function_adds_userto_list_users(self):
        result = self.myuser.addUser()
        message = {"me@gmail":["melvin","password"]}
        self.assertEqual(result,message)
        
    
if __name__ == '__main__':
    unittest.main()