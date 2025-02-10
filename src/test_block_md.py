import unittest
from block_markdown import *

class TestTextNode(unittest.TestCase):

    test_str = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

    def test_block_simple(self):
        print(self.test_str)
        print(markdown_to_blocks(self.test_str))

    def test_block_type(self):
        t = block_to_block_type("parapara")
        print("tbt" + "*" * 24)
        print("tbt Testing block type check : heading")
        for i in range(9):
            print("tbt " + block_to_block_type("#" * i + " teet"))
        print("tbt" + "*" * 24)
        
    def test_block_type_code(self):
        test_head = "tbt_c"
        print(test_head + " " + "*" * 24)
        print(test_head + " Testing block type check : heading")
        print(test_head + " " + block_to_block_type("``` should be code ```"))
        print(test_head + " " + block_to_block_type("``` should NOT be code ```djkf"))
        print(test_head + " " + "*" * 24)

    def test_block_type_quote(self):
        test_head = "tbt_q"
        tstr = """>>>quote
>>>quotoeoe """
        print(test_head + " " + "*" * 24)
        print(test_head + " Testing block type check : quote")
        print(test_head + " " + block_to_block_type(tstr))
        tstr = """>>>quote
quotoeoe 
        kdjkdk"""
        print(test_head + " " + block_to_block_type(tstr))
        print(test_head + " " + "*" * 24)

    def test_block_type_list(self):
        tstr = """- dkfjd
- jdfkdj"""
        test_head = "tbtl"
        print(test_head + " " + "*" * 24)
        print(test_head + " Testing block type check : unordered")
        print(test_head + " " + block_to_block_type(tstr))
        print(test_head + " " + "*" * 24)
        tstr = """-dkfjd
- jdfkdj"""
        print(test_head + " Testing block type check : NOT unordered")
        print(test_head + " " + block_to_block_type(tstr))
        print(test_head + " " + "*" * 24)
        tstr = """1. -dkfjd
2. - jdfkdj"""
        print(test_head + " Testing block type check : ordered")
        print(test_head + " " + block_to_block_type(tstr))
        print(test_head + " " + "*" * 24)

