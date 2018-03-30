#######################################################
# To be finish latter, consider to use pytest-sanic
#######################################################
import os
import sys
sys.path.append(os.getcwd())
import unittest
from app.main import app


class BasicTestCase(unittest.TestCase):
    def test_get_demo_person_returns_200(self):
        request, response = app.test_client.get('/demo/person')
        self.assertEqual(response.status, 200)

    def test_demo_person_put_not_allowed(self):
        request, response = app.test_client.put('/demo/person')
        self.assertEqual(response.status, 405)


if __name__ == '__main__':
    unittest.main()
