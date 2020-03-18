# import unittest
# import json

# import astroimages_api.api.fits_files.fits_handler as fits_handler
# import astroimages_api.app as app

# class TestFitsFileHandler(unittest.TestCase):

#     def setUp(self):
#         self.BASE_URL = 'http://localhost:5000/api/v1/fits-files'
#         # self.BASE_URL = '/api/v1/fits-files'
#         # self.flask_app = app.app.test_client()
#         # self.flask_app.testing = True

#     # def test_get_fits_files(self):
#     #     "Testing the get_fits_files - Happy path."
#     #     response = fits_handler.get_fits_files()
#     #     print('RESPONSE = %s' + response)

#     # def test_get_fits_file(self):
#     #     "Testing the get_fits_file - Happy path."
#     #     response = fits_handler.get_fits_file(12)
#     #     print('RESPONSE = %s' + response)

#     # def test_list(self):
#     #     print('\n')
#     #     response = self.flask_app.get(self.BASE_URL)
#     #     print(str(response))
#         # data = json.loads(response.get_data())
#         # print(data)
#         # if data is not None:
#         #     self.assertEqual(response.status_code, 200)


# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestFitsFileHandler)
#     unittest.TextTestRunner(verbosity=2).run(suite)
