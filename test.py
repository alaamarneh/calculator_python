#some text2
import unittest
import json

from main import app

class TestURLShorten(unittest.TestCase):
    client = None
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_get(self):
        rv = self.client.get("/?arg1=2&arg2=3&op=add")
        json = rv.json()
        print (json['result'])
        self.assertTrue(float(json['result']) == 5)
        self.assertTrue(rv.status_code == 200)

if __name__ == '__main__':
    unittest.main()