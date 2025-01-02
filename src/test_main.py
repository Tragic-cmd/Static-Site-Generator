import unittest
from main import extract_title

class Test_Extract_Title(unittest.TestCase):
    def test_valid_h1_title(self):
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_no_title(self):
        markdown = "No h1 here\nJust regular text"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_leading_whitespace(self):
        markdown = "#    Hello World   "
        self.assertEqual(extract_title(markdown), "Hello World")


if __name__ == "__main__":
    unittest.main()