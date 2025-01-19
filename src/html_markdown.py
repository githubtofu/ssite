import re
from block_markdown import *
from inline_markdown import *
from htmlnode import *

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")

def get_num_marks(text, block_type):
    if block_type == "heading":
        r = re.compile(r"(#+) ")
        return len(r.match(text).group(1))

def text_to_children(text):
    return list(map(text_node_to_html_node, text_to_textnodes(text)))

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for a_block in blocks:
        block_type = block_to_block_type(a_block)
        print(f"block type found :{block_type}:{a_block}")
        child_nodes = []
        if block_type == "ul" or block_type == "ol":
            child_blocks = a_block.split('\n')
            for a_child_block in child_blocks:
                grand_child_nodes = text_to_children(a_child_block[a_child_block.find(' ')+1:])
                child_nodes.append(ParentNode("li", grand_child_nodes))
        elif not block_type == "p": 
            child_nodes = text_to_children(a_block[a_block.find(' ')+1:])
        else:
            child_nodes = text_to_children(a_block)
        print(f"children nodes are :{child_nodes}:")
        if block_type == "heading":
            html_node = ParentNode("h"+str(get_num_marks(a_block, "heading"))
                                 , child_nodes)
        else:
            html_node = ParentNode(block_type, child_nodes)
        block_nodes.append(html_node)
    top_node = ParentNode("div", block_nodes)
    print(f"TOP NODE:{top_node}")
    return top_node



