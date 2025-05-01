import os
from pathlib import Path

from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    
    for filename in os.listdir(dir_path_content):
        src_path=os.path.join(dir_path_content,filename)
        dest_path=os.path.join(dest_dir_path,filename)
        if os.path.isfile(src_path):
            generate_page(src_path,template_path,Path(dest_path).with_suffix(".html"),basepath)
        else:
            generate_pages_recursive(src_path,template_path,dest_path,basepath)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f" * {from_path} {template_path} -> {dest_path}")
    with open(from_path,"r") as file:
        markdown_content=file.read()
    with open(template_path,"r") as file:
        template=file.read()
    
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    page_title=extract_title(markdown_content)
    template=template.replace("{{ Title }}",page_title)
    template=template.replace("{{ Content }}",html)
    template=template.replace('href="/',f'href="{basepath}')
    template=template.replace('src="/',f'src="{basepath}')
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path,"w") as file:
        file.write(template)


def extract_title(markdown):
    lines=markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
        raise ValueError("no title found")