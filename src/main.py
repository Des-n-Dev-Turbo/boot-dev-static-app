from textnode import TextNode, TextType
from markdown_to_html import markdown_to_html
import os
import sys


def copy_directory(src: str, dest: str):
    # ---- 1. DELETE DESTINATION ----
    if os.path.exists(dest):
        print(f"Deleting directory: {dest}")
        _delete_recursive(dest)

    # ---- 2. CREATE DESTINATION ----
    print(f"Creating directory: {dest}")
    os.mkdir(dest)

    # ---- 3. COPY ----
    _copy_recursive(src, dest)


# ---- DELETE RECURSIVELY ----
def _delete_recursive(path: str):
    if os.path.isfile(path):
        print(f"Deleting file: {path}")
        os.remove(path)
        return

    # Directory
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        _delete_recursive(item_path)

    print(f"Removing directory: {path}")
    os.rmdir(path)


# ---- COPY RECURSIVELY ----
def _copy_recursive(src: str, dest: str):
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        # ---- DIRECTORY ----
        if os.path.isdir(src_path):
            print(f"Creating directory: {dest_path}")
            os.mkdir(dest_path)
            _copy_recursive(src_path, dest_path)

        # ---- FILE ----
        else:
            print(f"Copying file: {src_path} → {dest_path}")
            _copy_file(src_path, dest_path)


# ---- FILE COPY (MANUAL) ----
def _copy_file(src: str, dest: str):
    with open(src, "rb") as f_src:
        with open(dest, "wb") as f_dest:
            while True:
                chunk = f_src.read(4096)  # 4KB chunks
                if not chunk:
                    break
                f_dest.write(chunk)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()  # removes "# " from start and trims whitespace
    raise Exception("No title found in markdown")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        markdown = f.read()

    with open(template_path) as f:
        template = f.read()

    html_node = markdown_to_html(markdown)
    html = html_node.to_html()

    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)

    template = template.replace("{{ Content }}", html)

    if basepath == "/":
        normalized_basepath = "/"
    else:
        normalized_basepath = basepath.rstrip("/") + "/"

    template = template.replace('href="/', f'href="{normalized_basepath}')
    template = template.replace('src="/', f'src="{normalized_basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dir_list = os.listdir(dir_path_content)

    for item in dir_list:
        item_path_content = os.path.join(dir_path_content, item)
        item_path_dest = os.path.join(dest_dir_path, item)

        if os.path.isdir(item_path_content):
            generate_pages_recursive(item_path_content, template_path, item_path_dest, basepath)
        elif item.endswith(".md"):
            dest_html_path = item_path_dest[:-3] + ".html"
            generate_page(item_path_content, template_path, dest_html_path, basepath)
            

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    print(basepath)

    copy_directory("static", "docs")

    generate_pages_recursive("content", "template.html", "docs", basepath)

main()