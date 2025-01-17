from textnode import TextNode, TextType
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for an_old_node in old_nodes:
        position = an_old_node.text.find(delimiter)
        if position == -1:
            new_nodes.append(an_old_node)
        else:
            closing_position = position + an_old_node.text[position+len(delimiter):].find(delimiter)
            if closing_position < position:
                new_nodes.append(an_old_node)
            else:
                closing_position += len(delimiter)
                if position > 0:
                    new_nodes.append(TextNode(an_old_node.text[:position], TextType.TEXT))
                new_nodes.append(TextNode(an_old_node.text[position+len(delimiter):closing_position], text_type))
                if closing_position < len(an_old_node.text):
                    new_nodes.append(TextNode(an_old_node.text[closing_position+len(delimiter):], TextType.TEXT))
    return new_nodes
