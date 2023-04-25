import mastergpt.src.Key as Key
import unittest
import mastergpt.src.Logger as Logger

API_KEY_TEST_VALUE = 'api_key_test'

class TestAPIKey(unittest.TestCase):

    def test_getKeys(self):
        self.assertEqual(Key.get_key_test(), API_KEY_TEST_VALUE, 'ERROR: API key test is not correct')
        Logger.debug('API key test is correct')