import unittest
from block_markdown import *

class TestTextNode(unittest.TestCase):
    def test_block_simple(self):
        test_str = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        print(test_str)
        print(markdown_to_blocks(test_str))




