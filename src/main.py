import os
import shutil
from md_to_html import markdown_to_html_node

def main():
    # Copy static files to public directory first
    copy_static_to_public()

    # Generate the main index HTML page
    generate_pages_recursive(
        dir_path_content="/home/tragic/workspace/github.com/tragic-cmd/Static-Site-Generator/content",
        template_path="/home/tragic/workspace/github.com/tragic-cmd/Static-Site-Generator/template.html",
        dest_dir_path="/home/tragic/workspace/github.com/tragic-cmd/Static-Site-Generator/public"
    )

def copy_static_to_public():
    stat_path = "/home/tragic/workspace/github.com/tragic-cmd/Static-Site-Generator/static"
    pub_path = "/home/tragic/workspace/github.com/tragic-cmd/Static-Site-Generator/public"

    if os.path.exists(pub_path):
        shutil.rmtree(pub_path)
    os.mkdir(pub_path)

    def copy_files(stat_path, pub_path):
        for item in os.listdir(stat_path):
            # Full path for the current item
            full_stat_path = os.path.join(stat_path, item)
            full_pub_path = os.path.join(pub_path, item)

            # You can now work with this path to determine if it's a file or directory
            if os.path.isfile(full_stat_path):
                shutil.copy(full_stat_path, full_pub_path)
            elif os.path.isdir(full_stat_path):
                # Make directory in destination if it doesn't exist
                if not os.path.exists(full_pub_path):
                    os.mkdir(full_pub_path)
                # Recursive call for directory
                copy_files(full_stat_path, full_pub_path)
    # Start the copying process
    copy_files(stat_path, pub_path)

def extract_title(markdown):
    blocks = markdown.split("\n")

    for line in blocks:
        if line.startswith("#"):
            cleaned_title = line.lstrip("#").strip()
            return cleaned_title
    raise Exception("No title found") 

def generate_page(from_path, template_path, dest_path):
    # Print a message about generating the page
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read markdown content from from_path
    with open(from_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()
    
    # Read template content from template_path
    with open(template_path, 'r', encoding='utf-8') as file:
        template_content = file.read()
    
    # Convert markdown to HTML using the markdown_to_html_node function
    # Assume markdown_to_html_node returns an object with a .to_html() method
    markdown_html_node = markdown_to_html_node(markdown_content)
    html_content = markdown_html_node.to_html()

    # Extract the title using extract_title
    title = extract_title(markdown_content)
    
    # Replace placeholders in the template
    full_html_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    # Ensure directory exists and write full HTML to dest_path
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w', encoding='utf-8') as file:
        file.write(full_html_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        full_content_path = os.path.join(dir_path_content, item)
        full_dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(full_content_path):
            if item.endswith(".md"):
                os.makedirs(os.path.dirname(full_dest_path), exist_ok=True)
                generate_page(full_content_path, template_path, full_dest_path.replace(".md", ".html"))
        else:
            generate_pages_recursive(full_content_path, template_path, full_dest_path)

if __name__ == "__main__":
    main()