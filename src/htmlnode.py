class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not implemented")

    def props_to_html(self):
        if self.props == None:
            return ""
        return f"{''.join(list(map(lambda x:f' {x[0]}=\"{x[1]}\"', self.props.items())))}"

    def __repr__(self):
        return f"HTMLNODE:(tag:{self.tag}, value:{self.value}, children:{self.children}, props:{self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("No value for a leaf node")
        if self.tag == None:
            return value
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag for a parent node")
        if self.children == None:
            raise ValueError("No children for parent node initialization")
        return f"<{self.tag} {self.props_to_html()}>{"".join(map(lambda x: x.to_html(), self.children))}</{self.tag}>"
