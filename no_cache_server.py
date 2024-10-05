import http.server
import socketserver

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

PORT = 8000
with socketserver.TCPServer(('', PORT), NoCacheHandler) as httpd:
    print(f'Serving at port {PORT}')
    httpd.serve_forever()

