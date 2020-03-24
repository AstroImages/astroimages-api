import unittest
import hashlib
import ntpath

from astroimages_api.api.fits_files.fits_service import FitsFileService
import astroimages_fits.fits_test_util_functions as ftuf

from astroimages_file_drivers.factory import get_file_driver
from astroimages_file_drivers.handler_enums import FILE_HANDLER_TYPE


class TestFitsFileService(unittest.TestCase):

    def setUp(self):
        self.total_files_per_folder = 2
        self.folder_handler, self.files_list = ftuf.create_empty_fits_files_on_temp_folder(
            self.total_files_per_folder)

        # print(self.files_list)
        # input("Press Enter to continue...")

        # TODO: FILE HANDLER TYPE should be injected (rsouza01)
        file_handler = get_file_driver(FILE_HANDLER_TYPE.NULL)

        self.fitsFileService = FitsFileService(self.folder_handler.name, file_handler)

    def tearDown(self):
        self.folder_handler.cleanup()

    def test_get_fits_files(self):
        files = self.fitsFileService.get_fits_files()
        self.assertEqual(len(files), self.total_files_per_folder)

    def test_get_fits_file(self):
        fileName = self.files_list[0].encode('utf-8')

        file = self.fitsFileService.get_fits_file(hashlib.md5(fileName).hexdigest(), True)

        self.assertNotEqual(file, None)
        self.assertEqual(file['title'], ntpath.basename(self.files_list[0]))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFitsFileService)
    unittest.TextTestRunner(verbosity=2).run(suite)
