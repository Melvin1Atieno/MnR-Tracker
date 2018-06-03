# class TestDevelopmentConfig(TestCase):


#     def create_app(self):
#         app.config.from_object('project.server.config.DevelopmentConfig')
#         return app 

#     def test_app_is_development(self):
#         """Test app is in developement"""
#         self.assertTrue(app.config["DEBUG"] is True)
#         self.assertFalse(current_app is None)

#     def test