
import unittest

from app.models  import User

class TestUserClass(unittest.TestCase):

    def setUp(self):
        self.myuser= User("me@gmail","melvin","password")

    def test_adduser_function_adds_userto_list_users(self):
        result = self.myuser.addUser()
        self.assertEqual(result,{"me@gmail":["melvin","password"]})
    
if __name__ == '__main__':
    unittest.main()