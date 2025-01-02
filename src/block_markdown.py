def markdown_to_blocks(markdown):
    # Initialize variables
    blocks = []
    current_block = []
    in_code_block = False
    
    for line in markdown.split("\n"):
        # Handle code blocks
        if line.startswith("```"):
            in_code_block = not in_code_block  # Toggle between True and False
            current_block.append(line)
            continue
        # Then handle the line based on whether we're in a code block
        if in_code_block:
            current_block.append(line)
        else:
            if line.startswith("#"):
                # First save any existing content
                if current_block:
                    blocks.append("\n".join(current_block))
                    current_block = []
                # Add heading as its own block
                blocks.append(line)
                # Skip the rest of the conditions
                continue
            if line.startswith(">"):
                # If we're not already building a quote block, save current block
                if not current_block or not current_block[-1].startswith(">"):
                    if current_block:
                        blocks.append("\n".join(current_block))
                        current_block = []
                # Add this quote line to the current block
                current_block.append(line)
                continue
            if line == "":
                if current_block:
                    blocks.append("\n".join(current_block))
                    current_block = []
            else:
                current_block.append(line)

    if current_block:
        blocks.append("\n".join(current_block))

    return blocks

def block_to_block_type(block):
    lines = block.split("\n")
    first_line = lines[0].strip()
    # Handle headings
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "heading"
    # Handle code blocks
    if lines[0].strip() == "```" and lines[-1].strip() == "```":
        return "code"
    # Handle quotes
    if block.startswith(">"):
        # Only check if non-empty lines start with ">"
        for line in lines:
            if line.strip() and not line.lstrip().startswith(">"):
                return "paragraph"
        return "quote"
    # Handle unordered lists (starting with "- " or "* ")
    if first_line.lstrip().startswith(("- ", "* ")):
        return "unordered_list"
    # Handle ordered lists (starting with number followed by period)
    if first_line.lstrip().split(". ")[0].isdigit():
        return "ordered_list"
    # Default to paragraph
    return "paragraph"