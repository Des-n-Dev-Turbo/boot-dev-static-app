from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue

        split_node = old_node.text.split(delimiter)

        if len(split_node) % 2 == 0:
            raise Exception("The Text is not properly using the md syntax")
        
        for i, text in enumerate(split_node):
            if i % 2 == 0:
                new_nodes.append(TextNode(text, TextType.TEXT))
            else:
                new_nodes.append(TextNode(text, text_type))


    return new_nodes