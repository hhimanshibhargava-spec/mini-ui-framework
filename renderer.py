import html
from element import Element


def render_to_html(element, handlers):
    """Turn an Element tree into an HTML string.

    `handlers` is a dictionary we fill in while rendering:
    it maps an event id (like "0") to the Python function to call.
    """
    # Plain text or numbers: just make them safe HTML text.
    if not isinstance(element, Element):
        return html.escape(str(element))

    # Copy the props so we don't change the original.
    props = dict(element.props)

    # "on_click" is special: it's a Python function, not an HTML attribute.
    on_click = props.pop("on_click", None)

    # Turn the remaining props into HTML attributes: class="title"
    attributes = ""
    for name, value in props.items():
        attributes += f' {name}="{html.escape(str(value), quote=True)}"'

    # Render all children first (this is the recursion).
    inner_html = ""
    for child in element.children:
        inner_html += render_to_html(child, handlers)

    tag_html = f"<{element.tag}{attributes}>{inner_html}</{element.tag}>"

    # If this element has a click handler, remember it and wrap the
    # element in a form that sends a POST request when clicked.
    if on_click is not None:
        event_id = str(len(handlers))   # "0", "1", "2", ...
        handlers[event_id] = on_click
        return (
            f'<form method="post" action="/event/{event_id}" class="event-form">'
            f"{tag_html}</form>"
        )

    return tag_html