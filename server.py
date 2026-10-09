from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    """Answers the browser's requests."""

    def do_GET(self):
        # The browser asks for the page.
        if self.path != "/":
            self.send_error(404)
            return
        body = self.server.app.page().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        # The browser says "a button was clicked": POST /event/<id>
        if not self.path.startswith("/event/"):
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", 0))
        self.rfile.read(length)             # read (and ignore) the form data
        event_id = self.path[len("/event/"):]

        self.server.app.handle_event(event_id)   # run the Python function

        # Tell the browser: "now go load / again" (it will get the new HTML).
        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()


def serve(app, port=8000):
    server = HTTPServer(("127.0.0.1", port), RequestHandler)
    server.app = app    # so RequestHandler can reach the app via self.server.app
    print(f"Running at http://127.0.0.1:{port}  (press Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")