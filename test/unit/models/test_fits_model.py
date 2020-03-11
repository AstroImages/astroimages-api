import unittest
from astroimages_api.models.fits_model import FitsFile

class TestFitsFile(unittest.TestCase):

    def test_json(self):
        fits = FitsFile('id', 'title', 'description', 'path')
        print('FitsFile = ' + fits.__repr__())
        #self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")


if __name__ == '__main__':
    unittest.main()
