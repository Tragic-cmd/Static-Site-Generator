import unittest
from htmlnode import HTMLNode

# This unittest is used to verify functionality of the htmlnode script
class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_single_prop(self):
        node = HTMLNode(
            tag="a",
            value="Click me!",
            props={"href": "https://www.google.com"}
        )
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode(
            tag="a",
            props={"href": "https://www.github.com", "target": "_blank"}
        )
        self.assertEqual(
        node.props_to_html(),
        ' href="https://www.github.com" target="_blank"'
    )

    def test_props_to_html_with_no_props(self):
        node = HTMLNode(tag="p", value="Hello world")
        self.assertEqual(node.props_to_html(), "")

if __name__ == '__main__':
    unittest.main()