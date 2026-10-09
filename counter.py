from framework import App, div, h1, p, button


# ---------- Event handlers (what happens on click) ----------

def increment():
    app.set_state(count=app.state["count"] + 1)

def decrement():
    app.set_state(count=app.state["count"] - 1)


# ---------- The component (what the UI looks like) ----------

def Counter(state):
    return div({"class": "counter"},
        h1({}, "Counter"),
        p({"class": "number"}, state["count"]),
        div({"class": "buttons"},
            button({"on_click": decrement}, "-"),
            button({"on_click": increment}, "+"),
        ),
    )


# ---------- Styling (plain CSS text) ----------

CSS = """
body { font-family: sans-serif; background: #f2f4f8; }
.counter { max-width: 260px; margin: 80px auto; padding: 24px;
           background: white; border-radius: 12px; text-align: center;
           box-shadow: 0 2px 8px rgba(0,0,0,0.15); }
.number { font-size: 56px; margin: 12px 0; }
.buttons { display: flex; justify-content: center; gap: 12px; }
.event-form { margin: 0; }
button { font-size: 24px; width: 56px; height: 48px; cursor: pointer; }
"""


# ---------- Create and run the app ----------

app = App(view=Counter, initial_state={"count": 0}, title="Counter", css=CSS)

if __name__ == "__main__":
    app.run()