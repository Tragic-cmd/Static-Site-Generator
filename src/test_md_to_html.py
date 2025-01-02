import unittest
from md_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        markdown = """This is a paragraph
that spans multiple lines.

This is another paragraph
with multiple lines too."""
        
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.tag, "div")
        self.assertEqual(len(node.children), 2)
        self.assertEqual(node.children[0].tag, "p")
        self.assertEqual(node.children[1].tag, "p")
        
    def test_headings(self):
        markdown = """# Heading 1
## Heading 2
### Heading 3"""
        
        node = markdown_to_html_node(markdown)
        self.assertEqual(len(node.children), 3)
        self.assertEqual(node.children[0].tag, "h1")
        self.assertEqual(node.children[1].tag, "h2")
        self.assertEqual(node.children[2].tag, "h3")
        
    def test_code_blocks(self):
        markdown = """```
def hello():
    return "world"
```"""
        
        node = markdown_to_html_node(markdown)
        self.assertEqual(len(node.children), 1)
        pre_node = node.children[0]
        self.assertEqual(pre_node.tag, "pre")
        self.assertEqual(len(pre_node.children), 1)
        self.assertEqual(pre_node.children[0].tag, "code")
        
    def test_nested_quotes(self):
        markdown = """> First level
>> Second level
> Back to first level"""
        
        node = markdown_to_html_node(markdown)
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].tag, "blockquote")

    def test_multiple_heading_levels(self):
        markdown = """# Heading 1
## Heading 2
# Another H1"""
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.children[0].tag, "h1")
        self.assertEqual(node.children[0].children[0].value, "Heading 1")
        self.assertEqual(node.children[1].tag, "h2")
        self.assertEqual(node.children[1].children[0].value, "Heading 2")
        self.assertEqual(node.children[2].tag, "h1")
        self.assertEqual(node.children[2].children[0].value, "Another H1")


    def test_heading_with_paragraph(self):
        markdown = """# Heading
This is a paragraph
with multiple lines."""
        node = markdown_to_html_node(markdown)
        self.assertEqual(len(node.children), 2)  # One heading, one paragraph
        self.assertEqual(node.children[0].tag, "h1")
        self.assertEqual(node.children[1].tag, "p")

    def test_code_block(self):
        markdown = "```\nprint('hello')\n```"
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.children[0].tag, "pre")
        self.assertEqual(node.children[0].children[0].tag, "code")

    def test_unordered_list(self):
        markdown = "- Item 1\n- Item 2"
        result = markdown_to_html_node(markdown)
        list_node = result.children[0]
        self.assertEqual(list_node.tag, "ul")
        self.assertEqual(list_node.children[0].tag, "li")
        self.assertEqual(list_node.children[0].children[0].value, "Item 1")
        self.assertEqual(list_node.children[1].tag, "li")
        self.assertEqual(list_node.children[1].children[0].value, "Item 2")

    def test_ordered_list(self):
        markdown = "1. Item one\n2. Item two"
        result = markdown_to_html_node(markdown)
        list_node = result.children[0]
        self.assertEqual(list_node.tag, "ol")
        self.assertEqual(list_node.children[0].tag, "li")
        self.assertEqual(list_node.children[0].children[0].value, "Item one")
        self.assertEqual(list_node.children[1].tag, "li")
        self.assertEqual(list_node.children[1].children[0].value, "Item two")

    def test_empty_document(self):
        markdown = ""
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.tag, "div")
        self.assertEqual(len(node.children), 0)  # Expecting no children for an empty document


class Test_Nested_Lists(unittest.TestCase):
    def test_nested_lists(self):
        markdown = """1. First item
   - Nested bullet
   - Another nested bullet
2. Second item
   1. Nested number
   2. Another number
3. Third item"""
        
        node = markdown_to_html_node(markdown)
        
        # Test the structure is a div
        self.assertEqual(node.tag, "div")
        
        # Get the main ordered list
        ol_node = node.children[0]
        self.assertEqual(ol_node.tag, "ol")
        self.assertEqual(len(ol_node.children), 3)  # Should have 3 main items
        
        # Check first item and its nested list
        first_li = ol_node.children[0]
        self.assertEqual(first_li.tag, "li")
        nested_ul = first_li.children[1]  # [0] would be the text node "First item"
        self.assertEqual(nested_ul.tag, "ul")
        self.assertEqual(len(nested_ul.children), 2)  # Should have 2 nested bullets
        
        # Check second item and its nested list
        second_li = ol_node.children[1]
        self.assertEqual(second_li.tag, "li")
        nested_ol = second_li.children[1]
        self.assertEqual(nested_ol.tag, "ol")
        self.assertEqual(len(nested_ol.children), 2)  # Should have 2 nested numbers

    def test_nested_list_with_varying_indents(self):
        markdown = """
- Item 1
   - Nested Item 1
   - Nested Item 2
- Item 2
   - Nested Item 3
      - Deep Nested Item
   - Nested Item 4
- Item 3
"""
        node = markdown_to_html_node(markdown)
        
        # Test the structure is a div
        self.assertEqual(node.tag, "div")
        
        # Get the main unordered list
        ul_node = node.children[0]
        self.assertEqual(ul_node.tag, "ul")
        self.assertEqual(len(ul_node.children), 3)  # Should have 3 main items
        
        # Check second item and its nested structure
        second_li = ul_node.children[1]  # Item 2
        self.assertEqual(second_li.tag, "li")
        
        # Check its nested list
        nested_ul = second_li.children[1]  # The nested list under Item 2
        self.assertEqual(nested_ul.tag, "ul")
        self.assertEqual(len(nested_ul.children), 2)  # Should have 2 nested items
        
        # Check the deeply nested item
        deep_nested_ul = nested_ul.children[0].children[1]  # The deepest nested list
        self.assertEqual(deep_nested_ul.tag, "ul")
        self.assertEqual(len(deep_nested_ul.children), 1)  # Should have 1 deep nested item

    def test_mixed_list_types(self):
        markdown = """1. First numbered item
   - Bullet point
   - Another bullet
2. Second numbered item
   1. Nested number
      - Deep bullet
      - Another deep bullet
   2. Another nested number
3. Third numbered item"""
        node = markdown_to_html_node(markdown)
        
        # Basic structure checks
        self.assertEqual(node.tag, "div")
        ol_node = node.children[0]
        self.assertEqual(ol_node.tag, "ol")
        self.assertEqual(len(ol_node.children), 3)
        
        # Check nested list under first item
        first_li = ol_node.children[0]
        nested_ul = first_li.children[1]
        self.assertEqual(nested_ul.tag, "ul")
        
        # Check deep nesting under second item
        second_li = ol_node.children[1]
        nested_ol = second_li.children[1]
        self.assertEqual(nested_ol.tag, "ol")
        deep_ul = nested_ol.children[0].children[1]
        self.assertEqual(deep_ul.tag, "ul")

    def test_empty_items(self):
        markdown = """- First item
- 
- Third item
   - Nested item
   - 
   - Another nested item"""
        node = markdown_to_html_node(markdown)
        
        ul_node = node.children[0]
        self.assertEqual(len(ul_node.children), 3)
        
        # Check that empty items are handled
        second_li = ul_node.children[1]
        self.assertEqual(len(second_li.children), 0)

    def test_complex_mixed_indentation(self):
        markdown = """1. Top level
   - Second level bullet
      1. Third level number
         - Fourth level bullet
   - Back to second level
2. Back to top
   1. Another second level
      - Third level bullet
         1. Fourth level number"""
        node = markdown_to_html_node(markdown)
        
        # Basic structure
        self.assertEqual(node.tag, "div")
        ol_node = node.children[0]
        self.assertEqual(ol_node.tag, "ol")
        
        # First top-level item
        first_li = ol_node.children[0]
        first_nested_ul = first_li.children[1]
        self.assertEqual(first_nested_ul.tag, "ul")
        
        # Check the deepest nesting under first item
        third_level = first_nested_ul.children[0].children[1]
        self.assertEqual(third_level.tag, "ol")
        fourth_level = third_level.children[0].children[1]
        self.assertEqual(fourth_level.tag, "ul")

if __name__ == "__main__":
    unittest.main()
