import unittest

import astroimages_api.api.fits_files.fits_handler as fits_handler
import astroimages_api.app as app


@unittest.skip("Skipping TestFitsFileHandler.")
class TestFitsFileHandler(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True
        
    def test_get_fits_files(self):
        "Testing the get_fits_files - Happy path."

        response = fits_handler.get_fits_files()
        print('RESPONSE = %s' + response)

    def test_get_fits_file(self):
        "Testing the get_fits_file - Happy path."

        response = fits_handler.get_fits_file(12)
        print('RESPONSE = %s' + response)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFitsFileHandler)
    unittest.TextTestRunner(verbosity=2).run(suite)
