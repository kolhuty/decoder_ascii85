import unittest
import base64
from decoding import decode
from encoding import encode

class TestEncoding(unittest.TestCase):
    def setUp(self):
        self.test_data = b"Hello, World!"
        self.encoded_data = base64.a85encode(self.test_data)
        self.invalid_data = b"vvwwx"

    def test_encode(self):
        result = encode(self.test_data)
        self.assertEqual(base64.a85decode(result), self.test_data)

    def test_decode(self):
        result = decode(self.encoded_data)
        self.assertEqual(result, self.test_data)

    def test_decode_error(self):
        with self.assertRaises(ValueError):
            decode(self.invalid_data)


if __name__ == '__main__':
    unittest.main()