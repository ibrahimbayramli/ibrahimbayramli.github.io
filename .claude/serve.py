#!/usr/bin/env python3
"""SPA-aware HTTP server: serves index.html for unknown routes."""
import os, sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8787
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class SPAHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def send_error(self, code, message=None, explain=None):
        if code == 404:
            self.path = '/index.html'
            return self.do_GET()
        super().send_error(code, message, explain)

    def log_message(self, fmt, *args):
        pass  # silence logs

HTTPServer(('', PORT), SPAHandler).serve_forever()
