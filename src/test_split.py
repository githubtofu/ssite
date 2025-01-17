import unittest
from textnode import TextNode, TextType
from parser import *

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
