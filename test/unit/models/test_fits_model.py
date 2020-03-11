import unittest
import json

from astroimages_api.models.fits_model import FitsFile

class TestFitsFile(unittest.TestCase):

    def test_json(self):
        fits = FitsFile('id', 'title', 'description', 'path')
        should_be = '{"id": "id", "title": "title", "description": "description", "path": "path"}'

        a, b = json.dumps(fits.__repr__(), sort_keys=True), json.dumps(should_be, sort_keys=True)

        self.assertEqual(a, b, "Should be %s" % should_be)


if __name__ == '__main__':
    unittest.main()
