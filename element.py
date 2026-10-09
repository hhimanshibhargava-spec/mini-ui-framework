class Element:
    """One node in the UI tree: a tag, some props, and some children."""

    def __init__(self, tag, props=None, children=None):
        self.tag = tag                  # e.g. "div", "button"
        self.props = props or {}        # e.g. {"class": "title"}
        self.children = children or []  # Elements or plain text/numbers


# Small helper functions so components read nicely.
# Usage: div({"class": "box"}, h1({}, "Hello"), p({}, "World"))

def div(props, *children):
    return Element("div", props, list(children))

def h1(props, *children):
    return Element("h1", props, list(children))

def p(props, *children):
    return Element("p", props, list(children))

def span(props, *children):
    return Element("span", props, list(children))

def button(props, *children):
    return Element("button", props, list(children))