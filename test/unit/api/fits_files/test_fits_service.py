import unittest
import hashlib

from astroimages_api.api.fits_files.fits_service import FitsFileService


class TestFitsFileService(unittest.TestCase):

    def setUp(self):
        folder = '/home/rsouza/Projects/AstroImages/FITS_FOLDER'
        self.fitsFileService = FitsFileService(folder)

    def test_get_fits_files(self):
        files = self.fitsFileService.get_fits_files()
        self.assertEqual(len(files), 2)

    def test_get_fits_file(self):
        fileName = b'/home/rsouza/Projects/AstroImages/FITS_FOLDER/FOCx38i0101t_c0f.fits'

        file = self.fitsFileService.get_fits_file(hashlib.md5(fileName).hexdigest(), True)
        print(file)

        self.assertNotEqual(file, None)
        self.assertEqual(file['title'], 'FOCx38i0101t_c0f.fits')
        self.assertEqual(file['primaryHDU']['BITPIX'], -32)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFitsFileService)
    unittest.TextTestRunner(verbosity=2).run(suite)
