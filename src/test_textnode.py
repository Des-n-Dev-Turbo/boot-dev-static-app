import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()