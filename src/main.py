from textnode import TextNode, TextType
from html_markdown import *
import os, shutil, re

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f: markdown = f.read()
    with open(template_path) as f: template = f.read()
    html_string = markdown_to_html_node(markdown).to_html()
    title_string = extract_title(markdown)
    template = template.replace("{{ Title }}", title_string)
    template = template.replace("{{ Content }}", html_string)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f: f.write(template)

def publish_html(source, destination):
    print(f"COPYING {source} to {destination}")
    if not os.path.exists(source):
        raise Exception("Source directory/file not found")
    if os.path.exists(destination):
        shutil.rmtree(destination)
    if os.path.isfile(source):
       shutil.copy(source, destination) 
       return
    if not os.path.isfile(destination):
        os.makedirs(destination, exist_ok=True)
    for a_path in os.listdir(source):
        publish_html(os.path.join(source, a_path), os.path.join(destination, a_path))
    return

def extract_title(markdown):
    r = re.compile(r"^# (.+?)$", re.MULTILINE)
    match = r.search(markdown)
    if match == None:
        raise Exception("No title found")
    return match.group(1)

def generate_all(source, dest):
    for a_path in os.listdir(source):
        print(f"in {a_path} : is file {os.path.isfile(a_path)}")
        print(f"in {a_path} : is file {os.path.isfile(os.path.join(source, a_path))}")
        if os.path.isfile(os.path.join(source, a_path)):
            if os.path.splitext(a_path)[1] == ".md":
                print(f"Generate {a_path}")
                generate_page(os.path.join(source, a_path), "template.html", os.path.join(dest, a_path).rstrip("md") + "html")
            else:
                print(f"NOT MD {os.path.splitext(a_path)}")
        else:
            print(f"Calling from subdirectory:{source}->{dest}:")
            generate_all(os.path.join(source, a_path), os.path.join(dest, os.path.basename(a_path)))

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    publish_html("static", "public")
    #generate_page("content/index.md", "template.html", "public/index.html")
    generate_all("content", "public")

main()
