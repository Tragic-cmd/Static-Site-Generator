from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type.value
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else: 
            return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
    # Converts a TextNode to an HTMLNode
    if text_node.text_type is TextType.TEXT.value:
        # TextType.NORMAL: This should become a LeafNode with no tag, just a raw text value.
        return LeafNode(None, text_node.text)
    if text_node.text_type is TextType.BOLD.value:
        # TextType.BOLD: This should become a LeafNode with a "b" tag and the text
        return LeafNode("b", text_node.text)
    if text_node.text_type is TextType.ITALIC.value:
        # TextType.ITALIC: "i" tag, text
        return LeafNode("i", text_node.text)
    if text_node.text_type is TextType.CODE.value:
        # TextType.CODE: "code" tag, text
        return LeafNode("code", text_node.text)
    if text_node.text_type is TextType.LINK.value:
        # TextType.LINK: "a" tag, anchor text, and "href" prop
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type is TextType.IMAGE.value:
        # TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError("Unrecognized TextType: {text_node.text_type}.")