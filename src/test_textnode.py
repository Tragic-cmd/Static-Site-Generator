import unittest
from textnode import TextNode, TextType, text_node_to_html_node

# This unittest is used to verify functionality of the textnode script
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # test with matching strings
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq_url(self):
        # testing url comparison
        node3 = TextNode("This is a text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node3, node4)
    def test_not_eq_url(self):
        # testing url comparison
        node5 = TextNode("This is a text node", TextType.BOLD)
        node6 = TextNode("This is a text node", TextType.BOLD, "https://www.github.com/Tragic-cmd")
        self.assertNotEqual(node5, node6)
    def test_not_eq_type(self):
        # testing text_type comparison
        node7 = TextNode("This is a text node", TextType.BOLD)
        node8 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node7, node8)
    def test_not_eq_text(self):
        # testing text comparison
        node9 = TextNode("This is a test node", TextType.BOLD)
        node10 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node9, node10)
    def test_repr(self):
        node = TextNode("This is a text node", TextType.NORMAL, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, normal, https://www.boot.dev)", repr(node)
        )

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()