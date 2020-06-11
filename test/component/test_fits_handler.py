import unittest
import os

from astroimages_api.api.fits_files.fits_service import FitsFileService
from astroimages_file_drivers.factory import get_file_driver
from astroimages_file_drivers.handler_enums import FILE_HANDLER_TYPE


class TestFitsHandler(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_happyFlow(self):
        'HAPPY FLOW'

        folder_name = './test/data/'

        try:

            self.fitsFileService = FitsFileService(
                folder_name,
                get_file_driver(FILE_HANDLER_TYPE.LOCAL))

            files = self.fitsFileService.get_fits_files()

            self.assertEqual(len(files), 2)

            # fileName = self.files_list[0].encode('utf-8')

            print('>>> FILES =>')
            print(files)

            # file = self.fitsFileService.get_fits_file(hashlib.md5(fileName).hexdigest(), True)
            # self.assertNotEqual(file, None)
            # self.assertEqual(file['title'], ntpath.basename(self.files_list[0]))

        finally:
            pass


if __name__ == '__main__':
    unittest.main()
