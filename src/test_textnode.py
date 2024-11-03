import unittest
from textnode import TextNode, TextType

# This unittest is used to verify functionality of the textnode script
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # test with matching strings
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        # testing url comparison
        node3 = TextNode("This is a text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node3, node4)
    def test_not_eq(self):
        # testing url comparison
        node5 = TextNode("This is a text node", TextType.BOLD)
        node6 = TextNode("This is a text node", TextType.BOLD, "https://www.github.com/Tragic-cmd")
        self.assertNotEqual(node5, node6)
        # testing text_type comparison
        node7 = TextNode("This is a text node", TextType.BOLD)
        node8 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node7, node8)
        # testing text comparison
        node9 = TextNode("This is a test node", TextType.BOLD)
        node10 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node9, node10)


if __name__ == "__main__":
    unittest.main()