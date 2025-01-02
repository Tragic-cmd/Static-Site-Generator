from block_markdown import markdown_to_blocks, block_to_block_type
from htmlnode import LeafNode, ParentNode
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes

def markdown_to_html_node(markdown):
    parent = ParentNode("div", [])
    blocks = markdown_to_blocks(markdown)
    block_nodes = []  # List to store all block nodes

    for block in blocks:
        type = block_to_block_type(block)
        tag = block_type_to_html_tag(type, block)

        if type == "code":
            # Handle nested code blocks
            lines = block.split("\n")
            cleaned_block = "\n".join(lines[1:-1])
            code_node = ParentNode(tag[1], [LeafNode("text", cleaned_block)]) # a "code" node
            pre_node = ParentNode(tag[0], [code_node]) # A "pre" node containing a code node
            block_nodes.append(pre_node)

        elif type in ["ordered_list", "unordered_list"]:
            items = block.split("\n")
            root_list_type = "ol" if items[0].lstrip().split('.')[0].isdigit() else "ul"
            root_list = ParentNode(root_list_type, [])
            
            current_lists = [root_list]  # Stack of active lists
            indent_levels = [0]  # Track indent levels separately
            
            for item in items:
                if item.strip() == "":
                    continue
                
                current_indent = len(item) - len(item.lstrip())
                stripped = item.lstrip()

                # Determine list item type and content
                if stripped.startswith(("*", "-", "+")) and stripped[2:].strip():
                    content = stripped[2:].strip()
                    list_type = "ul"
                else:
                    parts = stripped.split(". ", 1)
                    content = parts[1].strip() if len(parts) > 1 else ""
                    list_type = "ol"

                # Proceed only if there's content to process
                if content:
                    li_node = ParentNode("li", text_to_children(content))

                    if current_indent > indent_levels[-1]:
                        new_list = ParentNode(list_type, [])
                        current_lists[-1].children[-1].children.append(new_list)
                        current_lists.append(new_list)
                        indent_levels.append(current_indent)
                    elif current_indent < indent_levels[-1]:
                        while len(current_lists) > 1 and current_indent < indent_levels[-1]:
                            current_lists.pop()
                            indent_levels.pop()
                        
                    # Add the li_node to the current list
                    current_lists[-1].children.append(li_node)

            block_nodes.append(root_list)

        elif type in ["heading", "paragraph"]:
            if type == "heading":
                level = 0
                for char in block:
                    if char == '#':
                        level += 1
                    else:
                        break
                # Create the appropriate heading tag (h1, h2, etc.)
                level = min(max(level, 1), 6)
                tag = f"h{level}"
                content = block.lstrip('#').lstrip().strip()

            else:
                tag = "p"
                content = block
            node = ParentNode(tag, text_to_children(content))
            block_nodes.append(node)

        elif type == "quote":
            lines = block.split('\n')
            # Create the root blockquote
            root_node = ParentNode("blockquote", [])
            current_node = root_node
            prev_depth = 0

            for line in lines:
                # Count the quote depth (number of '>')
                depth = 0
                while depth < len(line) and line[depth] == '>':
                    depth += 1
                
                # Get the actual content after removing '>' characters
                content = line[depth:].lstrip()
                
                # Handle nesting
                if depth > prev_depth:
                    # Need to create new nested blockquote
                    for _ in range(depth - prev_depth):
                        new_node = ParentNode("blockquote", [])
                        current_node.children.append(new_node)
                        current_node = new_node
                elif depth < prev_depth:
                    # Need to go back up the tree
                    for _ in range(prev_depth - depth):
                        current_node = root_node  # Go back to parent
                
                # Add the content to current level if there is any
                if content:
                    current_node.children.extend(text_to_children(content))
                
                prev_depth = depth
            
            block_nodes.append(root_node)


    parent.children = block_nodes  # Add all nodes as children to parent div
    return parent  # Return the complete tree

def block_type_to_html_tag(type, block):
    if type == "paragraph":
        return "p"
    if type == "quote":
        return "blockquote"
    if type == "heading":
        n = count_leading_hash(block)
        return f"h{n}"
    if type == "code":
        return ("pre", "code")  # Return both tags as a tuple
    if type == "unordered_list":
        return "ul"
    if type == "ordered_list":
        return "ol"
    
def text_to_children(text):
    # Convert text to TextNodes using your existing function
    nodes = text_to_textnodes(text)
    # Convert TextNodes to HTMLNodes
    html_nodes = []
    for node in nodes:
        html_node = text_node_to_html_node(node)
        if html_node is not None:
            html_nodes.append(html_node)
    return html_nodes

def count_leading_hash(block):
    count = 0
    for char in block:
        if char != '#':
            break
        count += 1
    return count