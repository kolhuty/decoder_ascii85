#!/usr/bin/env python3

import unittest
import ascii85
import base64

class TestEncoder(unittest.TestCase):

    def setUp(self):
        self.encoded_data = base64.a85encode(b'test')
        self.decoded_data = b'test'

    def test_encode(self):
        """Проверка encode_data"""
        result = ascii85.encode(self.decoded_data)
        self.assertEqual(base64.a85decode(result), self.decoded_data)

    def test_decode(self):
        """Проверка decode_data"""
        result = ascii85.decode(self.encoded_data)
        self.assertEqual(result, self.decoded_data)



if __name__ == '__main__':
    unittest.main()