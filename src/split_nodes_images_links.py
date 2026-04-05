from utils import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        extracted_images = extract_markdown_images(old_node.text)

        if len(extracted_images) == 0:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text

        for image_data in extracted_images:
            section = original_text.split(f"![{image_data[0]}]({image_data[1]})", 1)

            if len(section) != 2:
                raise ValueError("Invalid markdown image syntax")
        
            if section[0] != "":
                new_nodes.append(TextNode(section[0], TextType.TEXT))
                
            new_nodes.append(TextNode(image_data[0], TextType.IMAGE, image_data[1]))

            original_text = section[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes

            
def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        extracted_links = extract_markdown_links(old_node.text)

        if len(extracted_links) == 0:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text

        for link_data in extracted_links:
            section = original_text.split(f"[{link_data[0]}]({link_data[1]})", 1)
            if len(section) != 2:
                raise ValueError("Invalid markdown link syntax")
            
            if section[0] != "":
                new_nodes.append(TextNode(section[0], TextType.TEXT))
                
            new_nodes.append(TextNode(link_data[0], TextType.LINK, link_data[1]))

            original_text = section[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes