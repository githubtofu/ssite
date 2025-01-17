import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("i", text_node.text)
        case TextType.LINKS:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case TextType.IMAGES:
            return LeafNode("img", {"src":text_node.url, "alt":text_node.text})


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_neq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "http something")
        node2 = TextNode("This is a text node", TextType.BOLD, "http something else")
        self.assertNotEqual(node, node2)

    def test_none_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "http something")
        node2 = TextNode("This is a text node", TextType.ITALIC, "http something")
        self.assertNotEqual(node, node2)

    def test_none_url(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC, None)
        self.assertEqual(node, node2)

    def test_t2h(self):
        node_italic = text_node_to_html_node(TextNode("This is a text node", TextType.ITALIC))
        node_link = text_node_to_html_node(TextNode("This is a text node", TextType.LINKS, "http link link"))
        node_image = text_node_to_html_node(TextNode("This is a text node", TextType.IMAGES, "http link link"))
        print(f"ITALIC:{node_italic}:")
        print(f"LINK:{node_link}:")
        print(f"IMAGE:{node_image}:")

if __name__ == "__main__":
    unittest.main()

