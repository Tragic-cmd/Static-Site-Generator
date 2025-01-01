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
