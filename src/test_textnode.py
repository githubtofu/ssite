import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode
from inline_markdown import *

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("i", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case TextType.IMAGE:
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
        node_link = text_node_to_html_node(TextNode("This is a text node", TextType.LINK, "http link link"))
        node_image = text_node_to_html_node(TextNode("This is a text node", TextType.IMAGE, "http link link"))
        print(f"ITALIC:{node_italic}:")
        print(f"LINK:{node_link}:")
        print(f"IMAGE:{node_image}:")

    def test_t2t(self):
        test_text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result=text_to_textnodes(test_text)
        print("*" * 35)
        print("Testing text to textnode")
        print(result)
        print("*" * 35)

if __name__ == "__main__":
    unittest.main()

