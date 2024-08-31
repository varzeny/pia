# util/read_from_file.py

# lib
from markdown import markdown

# module

# attribute

# method
def read_markdown_from_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        content = f.read()
    
    html_content = markdown(content)

    return html_content