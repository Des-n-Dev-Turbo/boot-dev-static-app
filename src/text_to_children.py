from textnode import text_node_to_html, text_node_to_html_node
from text_to_textnodes import text_to_textnodes

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = [text_node_to_html_node(text_node) for text_node in text_nodes]
    return children