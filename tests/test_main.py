import unittest
from unittest.mock import patch
import sys
import io
import ascii85

class TestMain(unittest.TestCase):

    @patch("sys.stderr", new_callable=io.StringIO)
    def test_main_arg_error(self, mock_stderr):
        with patch("sys.argv", ["script.py", "-x"]):
            with self.assertRaises(SystemExit) as cm:
                ascii85.main()
            self.assertEqual(cm.exception.code, 1)

    @patch("ascii85.handle_encoding")
    @patch("sys.argv", ["script.py"])
    def test_main_default_encode(self, mock_handle):
        ascii85.main()
        mock_handle.assert_called_once()

    @patch("ascii85.handle_decoding")
    @patch("sys.argv", ["script.py", "-d"])
    def test_main_decode(self, mock_handle):
        ascii85.main()
        mock_handle.assert_called_once()

    #Тест прерывания операции
    @patch("sys.stderr", new_callable=io.StringIO)
    @patch("sys.exit")
    @patch("ascii85.handle_encoding", side_effect=KeyboardInterrupt)
    def test_main_keyboard_interrupt(self, mock_handle, mock_exit, mock_stderr):
        with patch("sys.argv", ["script.py"]):
            ascii85.main()
            mock_exit.assert_called_once_with(4)

class TestCLI(unittest.TestCase):
    def test_parse_arguments(self):
        test_cases = [
            (["-e"], {"encode": True, "decode": False, "error": None}),
            (["-d"], {"encode": False, "decode": True, "error": None}),
            (["--help"], {"help": True}),
            (["-e", "-d"], {"error": "Cannot use both -e and -d"}),
            (["-x"], {"error": "Unknown options: -x"})
        ]

        for args, expected in test_cases:
            with self.subTest(args=args):
                result = ascii85.parse_arguments(args)
                for key in expected:
                    self.assertEqual(result[key], expected[key])

if __name__ == "__main__":
    unittest.main()