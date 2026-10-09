from renderer import render_to_html
from server import serve


class App:
    """Holds the state, re-renders when it changes, and runs the server."""

    def __init__(self, view, initial_state, title="My App", css=""):
        self.view = view                    # a function: state -> Element tree
        self.state = dict(initial_state)    # the app's data
        self.title = title
        self.css = css
        self.handlers = {}                  # event id -> Python function
        self.body_html = ""                 # the latest rendered HTML
        self.render()                       # first render

    def set_state(self, **changes):
        """Change the state, then re-render the UI."""
        self.state.update(changes)
        self.render()

    def render(self):
        """Build a fresh element tree from the current state, then make HTML."""
        self.handlers = {}                  # start with a clean handler list
        tree = self.view(self.state)        # call the user's component function
        self.body_html = render_to_html(tree, self.handlers)

    def handle_event(self, event_id):
        """Find the function for this event id and run it."""
        handler = self.handlers.get(event_id)
        if handler is not None:
            handler()                       # the handler calls set_state()

    def page(self):
        """The full HTML page that the browser receives."""
        return (
            "<!DOCTYPE html>"
            '<html><head><meta charset="utf-8">'
            f"<title>{self.title}</title>"
            f"<style>{self.css}</style>"
            f"</head><body>{self.body_html}</body></html>"
        )

    def run(self, port=8000):
        serve(self, port)