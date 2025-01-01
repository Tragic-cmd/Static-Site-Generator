import re

def markdown_to_blocks(markdown):
    lines = []
    new_lines = []
    section = ""
    lines = markdown.split("\n")
    
    for line in lines:
        if line != "":
            if section != "": 
                section += f"\n{line}"
            else:
                section = line
        else:
            if section:
                new_lines.append(section)
                section = ""
    
    # Append the last section if not empty
    if section:
        new_lines.append(section)
        
    return new_lines

def block_to_block_type(block):
    block_type = ""
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        block_type = "heading"
    elif block.startswith("```") and block.endswith("```"):
        block_type = "code"
    elif block.startswith(">"):
        is_valid = True
        lines = block.split("\n")
        for line in lines: 
            if not line.startswith(">"):
                is_valid = False
                break
        if is_valid:
            block_type = "quote"
    elif block.startswith(("* ", "- ")):
        is_valid = True
        lines = block.split("\n")
        for line in lines: 
            if not line.startswith(("* ", "- ")):
                is_valid = False
                break
        if is_valid:
            block_type = "unordered_list"
    elif block.startswith("1. "):
        is_valid = True
        n = 0
        lines = block.split("\n")
        for line in lines: 
            n += 1
            if not line.startswith(f"{n}. "):
                is_valid = False
                break
        if is_valid:
            block_type = "ordered_list"
    else: 
        block_type = "paragraph"
    return block_type


