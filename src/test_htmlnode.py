import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):
    def test_single_parent_and_child(self):
        # Test case 1 - Simple parent with one child
        node1 = ParentNode("div", [
            LeafNode("p", "Hello")
        ])
        self.assertEqual(node1.to_html(), "<div><p>Hello</p></div>")

    def test_multiple_children(self):
        # Test case 2 - Parent with multiple children
        node2 = ParentNode("div", [
            LeafNode("p", "First"),
            LeafNode("p", "Second")
        ])
        self.assertEqual(node2.to_html(), "<div><p>First</p><p>Second</p></div>")

    def test_nested_parents(self):
        # Test case 3 - Parent nodes nested within parent nodes
        node3 = ParentNode("div", [
            ParentNode("p", [
                LeafNode("span", "Nested")
            ])
        ])
        self.assertEqual(node3.to_html(), "<div><p><span>Nested</span></p></div>")

    def test_no_tag(self):
        # Test that ValueError is raised when tag is None
        node5 = ParentNode(None, [
            LeafNode("p", "Hello")
        ])
        with self.assertRaises(ValueError):
            node5.to_html()

    def test_no_children(self):
        # Test that ValueError is raised with empty children list
        node6 = ParentNode("div", [])
        with self.assertRaises(ValueError):
            node6.to_html()




if __name__ == '__main__':
    unittest.main()