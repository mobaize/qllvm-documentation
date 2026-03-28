#!/usr/bin/env python3
"""
自定义HTTP服务器，为.txt文件设置正确的Content-Type头
"""

import http.server
import socketserver
import os

PORT = 8002

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # 为.txt文件设置正确的Content-Type头
        if self.path.endswith('.txt'):
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
        super().end_headers()

if __name__ == "__main__":
    # 切换到build/html目录
    os.chdir('build/html')
    
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"服务器运行在 http://localhost:{PORT}")
        print("按 Ctrl+C 停止服务器")
        httpd.serve_forever()
