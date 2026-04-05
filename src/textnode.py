from enum import Enum
from unittest import case
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__ (self, text, text_type: TextType, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: "TextNode"):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            text = LeafNode(None, text_node.text, None)
            return text.to_html()
        case TextType.BOLD:
            text = LeafNode("b", text_node.text, None)
            return text.to_html()
        case TextType.ITALIC:
            text = LeafNode("i", text_node.text, None)
            return text.to_html()
        case TextType.CODE:
            text = LeafNode("code", text_node.text, None)
            return text.to_html()
        case TextType.LINK:
            text = LeafNode("a", text_node.text, {"href": text_node.url})
            return text.to_html()
        case TextType.IMAGE:
            text = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
            return text.to_html()
        case _:
            raise Exception('Not a valid text type')
        
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            text = LeafNode(None, text_node.text, None)
            return text
        case TextType.BOLD:
            text = LeafNode("b", text_node.text, None)
            return text
        case TextType.ITALIC:
            text = LeafNode("i", text_node.text, None)
            return text
        case TextType.CODE:
            text = LeafNode("code", text_node.text, None)
            return text
        case TextType.LINK:
            text = LeafNode("a", text_node.text, {"href": text_node.url})
            return text
        case TextType.IMAGE:
            text = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
            return text
        case _:
            raise Exception('Not a valid text type')