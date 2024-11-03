import unittest
from htmlnode import HTMLNode, LeafNode

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

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_with_tag_and_value(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_node_with_props(self):
        node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com"}
        )
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_node_without_tag(self):
        node = LeafNode(None, "Just plain text")
        self.assertEqual(node.to_html(), "Just plain text")

    def test_leaf_node_without_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

if __name__ == '__main__':
    unittest.main()