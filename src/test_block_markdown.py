import unittest
from block_markdown import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    
    def test_single_block(self):
        markdown = "# A single heading block"
        expected = ["# A single heading block"]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

    def test_multiple_blocks(self):
        markdown = "# Heading\n\nParagraph with **bold**.\n\n* Item 1\n* Item 2"
        expected = [
            "# Heading",
            "Paragraph with **bold**.",
            "* Item 1\n* Item 2"
        ]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)
    
    def test_with_leading_and_trailing_newlines(self):
        markdown = "\n\n# Heading\n\nParagraph\n\n\n"
        expected = [
            "# Heading",
            "Paragraph"
        ]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)
    
    def test_all_blank_lines(self):
        markdown = "\n\n\n\n"
        expected = []
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)
    
    def test_no_blank_lines(self):
        markdown = "First line\nSecond line\nThird line"
        expected = [
            "First line\nSecond line\nThird line"
        ]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()