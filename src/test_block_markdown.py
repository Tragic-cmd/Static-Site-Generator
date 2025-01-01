import unittest
from block_markdown import markdown_to_blocks, block_to_block_type

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

class TestBlockToBlockType(unittest.TestCase):

    def test_paragraph_block(self):
        markdown = "Just a normal paragraph"
        expected = "paragraph"
        result = block_to_block_type(markdown)
        self.assertEqual(result, expected)

    def test_heading_block(self):
        markdown = "# Heading 1"
        expected = "heading"
        result = block_to_block_type(markdown)
        self.assertEqual(result, expected)

    def test_heading_block_2(self):
        markdown = "### Heading 3"
        expected = "heading"
        result = block_to_block_type(markdown)
        self.assertEqual(result, expected)

    def test_code_block(self):
        markdown = "```\nsome code\n```"
        expected = "code"
        result = block_to_block_type(markdown)
        self.assertEqual(result, expected)

    def test_quote_block(self):
        markdown = "> List Item 1\n> List Item 2\n> List Item 3"
        expected = "quote"
        result = block_to_block_type(markdown)
        self.assertEqual(result, expected)

    def test_unordered_list_block(self):
        markdown = "* List Item 1\n* List Item 2\n* List Item 3"
        expected = "unordered_list"
        result = block_to_block_type(markdown)
        self.assertEqual(result, expected)

    def test_unordered_list_block_2(self):
        markdown = "- List Item 1\n- List Item 2\n- List Item 3"
        expected = "unordered_list"
        result = block_to_block_type(markdown)
        self.assertEqual(result, expected)

    def test_ordered_list_block(self):
        markdown = "1. List Item 1\n2. List Item 2\n3. List Item 3"
        expected = "ordered_list"
        result = block_to_block_type(markdown)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()