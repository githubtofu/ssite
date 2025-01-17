from textnode import *

def text_node_to_html_node(text_node):
    match text_node:
        case text_node.TEXT:
            return LeafNode(text_node.value)
        case text_node.BOLD:
            return LeafNode("b", text_node.value)
        case text_node.ITALIC:
            return LeafNode("i", text_node.value)
        case text_node.CODE:
            return LeafNode("i", text_node.value)
        case text_node.LINK:
            return LeafNode("a", text_node.value, {"href":text_node.url})
        case text_node.IMAGE:
            return LeafNode("img", {"src":text_node.url, "alt":text_node.value})
            
def main():
    my_node = TextNode("Test node", TextType.BOLD, "https:/nonese")
    print(my_node)


if __name__ == "__main__":
    main()
