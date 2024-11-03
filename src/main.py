from textnode import TextNode, TextType

def main():
    test_node = TextNode("Lets hope this works", TextType.NORMAL, "https://github.com/Tragic-cmd")
    print(test_node)


if __name__ == "__main__":
    main()