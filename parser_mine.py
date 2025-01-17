from textnode import TextNode, TextType
import re, functools

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for an_old_node in old_nodes:
        position = an_old_node.text.find(delimiter)
        if position == -1:
            new_nodes.append(an_old_node)
        else:
            closing_position = position + an_old_node.text[position+len(delimiter):].find(delimiter)
            if closing_position < position:
                new_nodes.append(an_old_node)
            else:
                closing_position += len(delimiter)
                if position > 0:
                    new_nodes.append(TextNode(an_old_node.text[:position], TextType.TEXT))
                new_nodes.append(TextNode(an_old_node.text[position+len(delimiter):closing_position], text_type))
                if closing_position < len(an_old_node.text):
                    new_nodes.append(TextNode(an_old_node.text[closing_position+len(delimiter):], TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    r = re.compile(r"!\[(.*?)\]\((.*?)\)")
    list_tuple_alt_url = []
    [list_tuple_alt_url.append((x.group(1), x.group(2))) for x in r.finditer(text)]
    return list_tuple_alt_url

def extract_markdown_links(text):
    r = re.compile(r"[^!]\[(.*?)\]\((.*?)\)")
    list_tuple_alt_url = []
    [list_tuple_alt_url.append((x.group(1), x.group(2))) for x in r.finditer(text)]
    return list_tuple_alt_url

def split_nodes_image(old_nodes):
    for an_old_node in old_nodes:
        r = re.compile(r"(.*?)!\[.*?\]\(.*?\)")
        match_first = r.match(an_old_node.text)
        list_text_node = [] if match_first == None else [TextNode(match_first.group(1), TextType.TEXT)]
        print(f"FIRSTNODE:{list_text_node}")
        r = re.compile(r"!\[(.*?)\]\((.*?)\)([^!]*)")
        matches = r.finditer(an_old_node.text)
        if matches != None:
            list_text_node += functools.reduce(lambda x, y: x + y, map(lambda x: [TextNode(x.group(1), TextType.IMAGES, x.group(2))]
                + ([] if x.group(3) == "" else [TextNode(x.group(3), TextType.TEXT)]), matches), [])
    return list_text_node

def split_nodes_link(old_nodes):
    for an_old_node in old_nodes:
        r = re.compile(r"(.*?)[^!]\[.*?\]\(.*?\)")
        match_first = r.match(an_old_node.text)
        print(f"FirstMATCH:{match_first}")
        list_text_node = [] if match_first == None else [TextNode(match_first.group(1), TextType.TEXT)]
        print(f"FIRSTNODE:{list_text_node}")
        #r = re.compile(r"[^!]\[(.*?)\]\((.*?)\)(.*)")
        r = re.compile(r"[^!]\[(.*?)\]\((.*?)\)(.*)(?=[^!]\[)")
        matches = r.finditer(an_old_node.text)
        if matches != None:
            list_text_node += functools.reduce(lambda x, y: x + y, map(lambda x: [TextNode(x.group(1), TextType.LINKS, x.group(2))]
                + ([] if x.group(3) == "" else [TextNode(x.group(3), TextType.TEXT)]), matches), [])
    return list_text_node
