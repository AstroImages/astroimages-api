import unittest
import json
from flask import current_app

import astroimages_api.api.fits_files.fits_handler as fits_handler
import astroimages_api.server as server

class TestFitsFileHandler(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        pass

    # executed after each test
    def tearDown(self):
        pass

    def test_get_fits_files(self):
        "Testing the get_fits_files - Happy path."

        with server.rest_app.test_client():
            with server.rest_app.app_context():
                response = fits_handler.get_fits_files()
                json_data = response.get_json()
                print('RESPONSE = %s' % json_data['fits_files'])

    # def test_get_fits_file(self):
    #     "Testing the get_fits_file - Happy path."
    #     response = fits_handler.get_fits_file(12)
    #     print('RESPONSE = %s' + response)

    # def test_list(self):
    #     print('\n')
    #     response = self.flask_app.get(self.BASE_URL)
    #     print(str(response))
        # data = json.loads(response.get_data())
        # print(data)
        # if data is not None:
        #     self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFitsFileHandler)
    unittest.TextTestRunner(verbosity=2).run(suite)
