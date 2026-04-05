import unittest

from textnode import TextNode, TextType, text_node_to_html


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.example.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, italic, https://www.example.com)")

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_neq_url(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.example.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https://www.example.org")
        self.assertNotEqual(node, node2)

    def test_empty_url(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK, None)
        self.assertEqual(node, node2)

    def test_text_node_to_html(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(text_node_to_html(node), "<b>This is a text node</b>")

    def test_text_node_to_html_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.example.com")
        self.assertEqual(text_node_to_html(node), '<a href="https://www.example.com">This is a link</a>')   

    def test_text_node_to_html_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.example.com/image.png")
        self.assertEqual(text_node_to_html(node), '<img src="https://www.example.com/image.png" alt="This is an image"></img>')

if __name__ == "__main__":
    unittest.main()