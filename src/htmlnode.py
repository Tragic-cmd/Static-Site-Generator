class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        string = ""
        if self.props is None:
            return string
        for key in self.props:
            string += f' {key}="{self.props[key]}"'
        return string

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)
        if self.value is None:
            raise ValueError
        
    def to_html(self):
        if self.tag is None:
            return self.value
        # format: <tag properties>value</tag>
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
