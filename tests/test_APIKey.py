from APIKey import APIKey
import unittest

API_KEY_TEST_VALUE = 'api_key_test'

class TestAPIKey(unittest.TestCase):

    def test_getKeys(self):
        self.assertEqual(APIKey().getKeyTest(), API_KEY_TEST_VALUE, 'ERROR: API key test is not correct')