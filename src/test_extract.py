import unittest
from textnode import TextNode, TextType
from inline_markdown import *

class TestExtractLinks(unittest.TestCase):
    def test_basic_extract(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        print("*" * 25)
        print("testing basic extract image link")
        print(extract_markdown_images(text))
        print("testing basic extract normal link")
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        print(extract_markdown_links(text))
        print("testing complex extract normal link")
        text = "This is text with a link [to boot dev](https://www.boot.dev) awith a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)nd [to youtube](https://www.youtube.com/@bootdotdev)"
        print("**LINK first**")
        print(extract_markdown_links(text))
        print("**IMG second**")
        print(extract_markdown_images(text))
        print("*" * 25)

