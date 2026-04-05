from split_nodes_images_links import split_nodes_image, split_nodes_link
from splitdelimiter import split_nodes_delimiter

from textnode import TextNode, TextType

def text_to_textnodes(text):
    text_nodes = [TextNode(text, TextType.TEXT)]

    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    text_nodes = split_nodes_link(text_nodes)
    text_nodes = split_nodes_image(text_nodes)

    return text_nodes