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

def block_to_block_type(block_text):
    print("tbt_q IN function print text")
    print(block_text)
    print("tbt_q" + "=" * 30)
    r = re.compile(r"#{1,6} .+")
    if r.match(block_text) != None:
        return "heading"
    r = re.compile(r"```.*?```$")
    if r.match(block_text) != None:
        return "code"
    r = re.compile(r"^[^>]", re.MULTILINE)
    if r.search(block_text) == None:
        return "quote"
    r = re.compile(r"")
    
    return "paragraph"
