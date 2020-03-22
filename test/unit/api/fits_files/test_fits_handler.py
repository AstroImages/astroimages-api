import unittest
import os

from werkzeug.exceptions import HTTPException

import astroimages_api.api.fits_files.fits_handler as fits_handler
import astroimages_fits.fits_test_util_functions as ftuf

import astroimages_api.server as server


class TestFitsFileHandler(unittest.TestCase):

    # executed prior to each test
    def setUp(self):

        self.should_print = False

        self.total_files_per_folder = 2
        self.folder_handler, self.files_list = ftuf.create_empty_fits_files_on_temp_folder(
            self.total_files_per_folder)

        os.environ['FITS_FOLDER'] = self.folder_handler.name

        server.rest_app.config["SERVER_NAME"] = 'testlocalhost'

        # print(self.files_list)
        # input("Press Enter to continue...")

    # executed after each test
    def tearDown(self):
        self.folder_handler.cleanup()

    def test_get_fits_files(self):
        "Testing the get_fits_files - Happy path."

        json_data = {}

        with server.rest_app.test_client():
            with server.rest_app.app_context():
                response = fits_handler.get_fits_files()
                json_data = response.get_json()

        if self.should_print:
            print('RESPONSE = %s' % json_data['fits_files'])

        self.assertEqual(len(json_data['fits_files']), self.total_files_per_folder)

    def test_get_fits_file(self):
        "Testing the get_fits_file - Happy path."

        # Getting files from folder.
        # It looks like cheating, but the files are created on the fly...
        with server.rest_app.test_client():
            with server.rest_app.app_context():
                response = fits_handler.get_fits_files()
                json_data = response.get_json()

        first_file = json_data['fits_files'][0]

        hash = first_file['id']

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
