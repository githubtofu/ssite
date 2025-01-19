import unittest

from htmlnode import *
from html_markdown import *

class TestHtmlNode(unittest.TestCase):
    def test_simple(self):
        node = HTMLNode(value="This is a HTML node", tag="p")
        node2 = HTMLNode(value="This is a HTML node", tag="a", children=[node])
        print(node)
        print(node2)
        self.assertEqual(node.tag, "p")

    def test_props(self):
        node = HTMLNode(value="This is a HTML node", tag="p")
        node2 = HTMLNode(value="This is a HTML node", tag="a", children=[node])
        print(node.props_to_html())
        print(node2.props_to_html())
        self.assertEqual(node.tag, "p")

    def test_props(self):
        node1_prop = {
                 "href": "HKGDKJK",
                 "target": "_blank"
                }
        node = HTMLNode(value="This is a HTML node", tag="p", props = node1_prop)
        node2 = HTMLNode(value="This is a HTML node", tag="a", children=[node])
        print(node.props_to_html())
        print(node2.props_to_html())
        self.assertEqual(node.tag, "p")

    def test_leaf(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print(node1.to_html())
        print("TEST LEAF check properties next line")
        print(node2.to_html())
        self.assertEqual(node2.tag, "a")

    def test_parent(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = ParentNode("a", [node1], {"href": "https://www.google.com"})
        print("NODE 1 LEAF")
        print(node1.to_html())
        print("NODE 2 Parent")
        print(node2.to_html())
        print("NODE 2 END")
        self.assertEqual(node2.tag, "a")

    def test_multi_children(self):
        node11 = LeafNode("p", "This is a first paragraph of text.")
        node12 = LeafNode("p", "This is a second paragraph of text.")
        node13 = LeafNode("p", "This is a yet another paragraph of text.")
        node1 = ParentNode("a", [node13], {"href": "https://www.google2.com"})
        node2 = ParentNode("a", [node11, node12, node1], {"href": "https://www.google.com"})
        print("MULTI NODE 2 Parent")
        print(node2.to_html())
        print("NODE 2 END")

    def test_final_html(self):
        tstr="""# Header
Paragraph

- list item
- list tem 2

[link](Something)
![image](some image)

startofstring __italicstring__ **boldstrint** simplestring **boldstring2** normal parag"""
        print("@"*40)
        print(markdown_to_html_node(tstr))
        print("@"*40)
