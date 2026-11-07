#!/usr/bin/env python3
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 8000

server = ThreadingHTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
print(f"Serving local lab on http://{HOST}:{PORT}")
print("Press Ctrl+C to stop.")
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nStopping local lab server.")
finally:
    server.server_close()
