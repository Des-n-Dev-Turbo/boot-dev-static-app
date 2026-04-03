import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("div", None, None, {"class": "container"})
        self.assertEqual(repr(node), "HTMLNode(div, None, None, {'class': 'container'})")

    def test_props_to_html(self):
        node = HTMLNode("div", None, None, {"class": "container", "id": "main"})
        self.assertEqual(node.props_to_html(), ' class="container" id="main"')

    def test_props_to_html_empty(self):
        node = HTMLNode("div")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_none(self):
        node = HTMLNode("div", None, None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty_dict(self):
        node = HTMLNode("div", None, None, {})
        self.assertEqual(node.props_to_html(), "")

    def test_repr_no_props(self):
        node = HTMLNode("div")
        self.assertEqual(repr(node), "HTMLNode(div, None, None, None)")

    def test_repr_with_children(self):
        child_node = HTMLNode("span", "Hello", None, {"class": "text"})
        node = HTMLNode("div", None, [child_node], {"class": "container"})
        self.assertEqual(repr(node), "HTMLNode(div, None, [HTMLNode(span, Hello, None, {'class': 'text'})], {'class': 'container'})")

    def test_repr_with_value(self):
        node = HTMLNode("p", "This is a paragraph.", None, {"class": "text"})
        self.assertEqual(repr(node), "HTMLNode(p, This is a paragraph., None, {'class': 'text'})")

    def test_throw_not_implemented(self):
        node = HTMLNode("div")
        with self.assertRaises(NotImplementedError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()
