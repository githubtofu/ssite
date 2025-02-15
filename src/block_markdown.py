<<<<<<< HEAD
import re

=======
import re, functools
>>>>>>> refs/remotes/origin/main
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

def block_to_block_type(block_text):
    r = re.compile(r"#{1,6} .+")
    if r.match(block_text) != None:
        return "heading"
    r = re.compile(r"```.*?```$")
    if r.match(block_text) != None:
        return "code"
    r = re.compile(r"^[^>]", re.MULTILINE)
    if r.search(block_text) == None:
        return "blockquote"
    lines = block_text.split('\n')
    if functools.reduce(lambda x, y: x and (y == "* " or y == "- "),
                        map(lambda x: x[:2], lines), True) == True:
        return "ul"
    list_index = 1
    for a_line in lines:
        r = re.compile(r"(\d+)\. ")
        match = r.match(a_line)
        if match == None:
            return "p"
        if int(match.group(1)) != list_index:
            return "p"
        list_index += 1
    return "ol"
