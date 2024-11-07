import re
from textnode import TextNode, TextType

patterns = {
    'bold': re.compile(r"\*\*(.*?)\*\*"),
    'italic': re.compile(r"\*(.*?)\*"),
    'link': re.compile(r"\[([^\[\]]*)\]\(([^\(\)]*)\)"),
    'image': re.compile(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"),
    'code': re.compile(r"\`([^`]*)\`"),
}

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT.value:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT.value:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT.value:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def find_next_match(text, start_position):
    earliest_match = None
    earliest_match_type = None

    for type, pattern in patterns.items():
        match = pattern.search(text, start_position)
        if match and (earliest_match is None or match.start() < earliest_match.start()):
            earliest_match = match
            earliest_match_type = type
    
    return earliest_match, earliest_match_type

def text_to_textnodes(text):
    current_position = 0
    new_nodes = []

    while current_position < len(text):
        # Find the next markdown match
        earliest_match, match_type = find_next_match(text, current_position)
        
        if earliest_match:
            # Extract and append plain text before this match (if any)
            if earliest_match.start() > current_position:
                plain_text = text[current_position:earliest_match.start()]
                new_nodes.append(TextNode(plain_text, TextType.TEXT))

                if match_type in ['code', 'bold', 'italic']:
                    segment = text[earliest_match.start():earliest_match.end()]

                    if match_type == 'code':
                        # Create a code node
                        new_nodes.extend(split_nodes_delimiter([TextNode(segment, TextType.TEXT)], "`", TextType.CODE))

                    elif match_type == 'bold':
                        # Create a bold node
                        new_nodes.extend(split_nodes_delimiter([TextNode(segment, TextType.TEXT)], "**", TextType.BOLD))

                    elif match_type == 'italic':
                        # Create an italic node
                        new_nodes.extend(split_nodes_delimiter([TextNode(segment, TextType.TEXT)], "*", TextType.ITALIC))

                else:
                    # Process the specific markdown match
                    if match_type == 'image':
                        # Extract and create the image node
                        for text, url in extract_markdown_images(segment):
                            node = TextNode(segment, TextType.IMAGE, url)
                            new_nodes.append(node)

                    elif match_type == 'link':
                        # Extract and create the link node
                        for text, url in extract_markdown_links(segment):
                            node = TextNode(segment, TextType.LINK, url)
                            new_nodes.append(node)

            # Update current position to past this match
            current_position = earliest_match.end()
        else:
            # Add the remaining text as plain text if no more matches
            new_nodes.append(TextNode(text[current_position:], TextType.TEXT))
            break

    return new_nodes


