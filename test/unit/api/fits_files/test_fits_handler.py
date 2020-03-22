import unittest

from werkzeug.exceptions import HTTPException

import astroimages_api.api.fits_files.fits_handler as fits_handler
import astroimages_api.server as server


class TestFitsFileHandler(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        self.should_print = False
        server.rest_app.config["SERVER_NAME"] = 'testlocalhost'

    # executed after each test
    def tearDown(self):
        pass

    def test_get_fits_files(self):
        "Testing the get_fits_files - Happy path."

        json_data = {}

        with server.rest_app.test_client():
            with server.rest_app.app_context():
                response = fits_handler.get_fits_files()
                json_data = response.get_json()

        if self.should_print:
            print('RESPONSE = %s' % json_data['fits_files'])

        self.assertEqual(len(json_data['fits_files']), 2)

    def test_get_fits_file(self):
        "Testing the get_fits_file - Happy path."

        hash = 'a59d38bc2bfe0a71c54ce366233997b1'

        json_data = {}

        with server.rest_app.test_client():
            with server.rest_app.app_context():
                response = fits_handler.get_fits_file(fits_file_id=hash)
                json_data = response.get_json()

        if self.should_print:
            print('RESPONSE = %s' % json_data['fits_file'])

        self.assertEqual(len(json_data['fits_file']), 1)

    def test_get_fits_file_not_found(self):
        "Testing the get_fits_file - File non existent."

        hash = 'SHOULD_NOT_BE_FOUND'
        error_code = 0

        try:
            with server.rest_app.test_client():
                with server.rest_app.app_context():
                    fits_handler.get_fits_file(fits_file_id=hash)
        except HTTPException as exception:
            error_code = exception.code

        self.assertEqual(error_code, 404)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFitsFileHandler)
    unittest.TextTestRunner(verbosity=2).run(suite)
