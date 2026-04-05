from block import BlockType
from parentnode import ParentNode
from text_to_children import text_to_children
from textnode import TextNode, TextType, text_node_to_html_node

    
def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)

    html = text_to_children(paragraph)
    return ParentNode("p", html)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break

    text = block[level + 1:]

    children = text_to_children(text)

    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    text = block[4:-3]  # removes "```\n" from start and "```" from end
    text_node = TextNode(text, TextType.TEXT)

    children = text_node_to_html_node(text_node)

    final_node = ParentNode(
        "pre",
        [ParentNode("code", [children])]
    )

    return final_node

def quote_to_html_node(block):
    lines = block.split("\n")
    quote_lines = [line.lstrip(">").strip() for line in lines]  # removes "> " from start of each line
    quote_text = "\n".join(quote_lines)

    children = text_to_children(quote_text)

    return ParentNode("blockquote", children)

def unordered_list_to_html_node(block):
    lines = block.split("\n")
    list_items = [line[2:] for line in lines]  # removes "- " from start of each line

    children = []
    for item in list_items:
        item_children = text_to_children(item)
        children.append(ParentNode("li", item_children))

    return ParentNode("ul", children)

def ordered_list_to_html_node(block):
    lines = block.split("\n")
    list_items = [line[line.find(". ") + 2:] for line in lines]  # removes "1. ", "2. ", etc. from start of each line

    children = []
    for item in list_items:
        item_children = text_to_children(item)
        children.append(ParentNode("li", item_children))

    return ParentNode("ol", children)


