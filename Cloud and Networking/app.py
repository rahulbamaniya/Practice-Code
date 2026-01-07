from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from Python app running in Docker!")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 5001), SimpleHandler)
    print("Server running on port 5001...")
    server.serve_forever()
