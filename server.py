#!/usr/bin/env python3
"""时光寄存 demo 静态服务器（端口 8899）"""
import http.server
import os
import socketserver

os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8899

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving 时光寄存 at http://127.0.0.1:{PORT}")
    httpd.serve_forever()
