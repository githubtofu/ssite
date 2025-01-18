import re, functools
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
    lines = block_text.split('\n')
    if functools.reduce(lambda x, y: x and (y == "* " or y == "- "),
                        map(lambda x: x[:2], lines), True) == True:
        return "unordered_list"
    list_index = 1
    for a_line in lines:
        print("tbtl checking line shown below")
        print(f"tbtl :{a_line}")
        r = re.compile(r"(\d+)\. ")
        match = r.match(a_line)
        if match == None:
            return "paragraph"
        print(f"tbtl :{match.group(1)}")
        if int(match.group(1)) != list_index:
            return "paragraph"
        list_index += 1
    return "ordered_list"
