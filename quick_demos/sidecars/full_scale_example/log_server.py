from http.server import BaseHTTPRequestHandler, HTTPServer
import sys

class LogHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        sys.stdout.write(body.decode('utf-8') + "\n")
        sys.stdout.flush()
        self.send_response(200)
        self.end_headers()

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), LogHandler)
    server.serve_forever()
