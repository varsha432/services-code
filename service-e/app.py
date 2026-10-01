import os
from http.server import BaseHTTPRequestHandler, HTTPServer

SERVICE=os.getenv("SERVICE_NAME", "service-e")
PORT=int(os.getenv("PORT", "8085"))
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body=b"ok"
            self.send_response(200)
        else:
            body=(SERVICE + "\n").encode()
            self.send_response(200)
        self.send_header("Content-Type","text/plain")
        self.send_header("Content-Length",str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def log_message(self,*args): pass
HTTPServer(("0.0.0.0",PORT),Handler).serve_forever()
