import unittest

from utils import extract_markdown_images, extract_markdown_links

class TestUtils(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is an image ![alt text](https://www.example.com/image.png) in markdown"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("alt text", "https://www.example.com/image.png")])

    def test_extract_markdown_links(self):
        text = "This is a link [example](https://www.example.com) in markdown"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("example", "https://www.example.com")])

    def test_extract_markdown_multiple_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_markdown_multiple_links(self):
        text = "This is text with a [boot dev](https://www.boot.dev) and [youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("boot dev", "https://www.boot.dev"), ("youtube", "https://www.youtube.com/@bootdotdev")])
