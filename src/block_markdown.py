import re

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    for a_block in blocks:
        a_block.strip()
    while True:
        if "" in blocks:
            blocks.remove("")
        else:
            break
    return blocks

def block_to_block_type(block_str):
    r = re.compile(r"")
