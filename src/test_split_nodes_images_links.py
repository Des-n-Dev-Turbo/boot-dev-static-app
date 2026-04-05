import unittest

from split_nodes_images_links import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodesImagesLinks(unittest.TestCase):
    def test_split_image_at_start(self):
        node = TextNode(
            "![image](https://example.com/img.png) trailing text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://example.com/img.png"),
                TextNode(" trailing text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_link_at_start(self):
        node = TextNode(
            "[boot.dev](https://boot.dev) is great",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("boot.dev", TextType.LINK, "https://boot.dev"),
                TextNode(" is great", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_image_no_images(self):
        node = TextNode(
            "Just plain text here",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("Just plain text here", TextType.TEXT)],
            new_nodes,
        )

    def test_split_link_no_links(self):
        node = TextNode(
            "Just plain text here",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [TextNode("Just plain text here", TextType.TEXT)],
            new_nodes,
        )

    def test_split_link_single_only(self):
        node = TextNode(
            "[Search](https://google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Search", TextType.LINK, "https://google.com"),
            ],
            new_nodes,
        )

    def test_split_non_text_node_unchanged(self):
        node = TextNode(
            "already bold",
            TextType.BOLD,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("already bold", TextType.BOLD)],
            new_nodes,
        )