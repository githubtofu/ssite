import unittest
from textnode import TextNode, TextType
from inline_markdown import *

class TestTextNode(unittest.TestCase):
    def test_basic_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        print("="*20)
        print("++testing split code++")
        print(new_nodes)
        print("++testing split bold")
        node2 = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes2 = split_nodes_delimiter([node2], "**", TextType.BOLD)
        print(new_nodes2)
        print("="*20)

    def test_image_split(self):
        node_text = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        node_image = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        new_nodes = split_nodes_image([node_image])
        print("*"*30)
        print("testing split images")
        print(new_nodes)
        print("*"*30)

    def test_links_split(self):
        node_text = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        node_image = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        new_nodes = split_nodes_link([node_image])
        print("*"*30)
        print("testing split links")
        print(new_nodes)
        print("*"*30)
