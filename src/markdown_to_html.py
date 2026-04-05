from helper import code_to_html_node, heading_to_html_node, ordered_list_to_html_node, quote_to_html_node, unordered_list_to_html_node, paragraph_to_html_node
from markdown_to_blocks import markdown_to_blocks
from block import block_to_block_type, BlockType
from parentnode import ParentNode

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING_1:
        return heading_to_html_node(block)
    if block_type == BlockType.HEADING_2:
        return heading_to_html_node(block)
    if block_type == BlockType.HEADING_3:
        return heading_to_html_node(block)
    if block_type == BlockType.HEADING_4:
        return heading_to_html_node(block)
    if block_type == BlockType.HEADING_5:
        return heading_to_html_node(block)
    if block_type == BlockType.HEADING_6:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)
    
    raise ValueError("invalid block type")

def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)

    nodes = []

    for block in blocks:
        nodes.append(block_to_html_node(block))

    return ParentNode("div", nodes)
