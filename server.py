import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
import os

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        query = urlparse.parse_qs(parsed_path.query)
        
        if self.path.startswith('/expansion') and 'n' in query:
            n = query['n'][0]
            process = subprocess.run(['expansion.exe'], input=n, text=True, capture_output=True)
            output = process.stdout.strip()

            filtered_output = output.split('Enter the value of n:')[-1].strip()
            
            filtered_output = filtered_output.replace('*', '')
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(filtered_output.encode())
        

        else:

            if self.path == '/':
                self.path = '/index.html'
            file_path = self.path.lstrip('/')
            
            if os.path.exists(file_path):
                self.send_response(200)
                if file_path.endswith('.html'):
                    self.send_header('Content-type', 'text/html')
                elif file_path.endswith('.css'):
                    self.send_header('Content-type', 'text/css')
                elif file_path.endswith('.js'):
                    self.send_header('Content-type', 'application/javascript')
                elif file_path.endswith('.png'):
                    self.send_header('Content-type', 'image/png')
                elif file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
                    self.send_header('Content-type', 'image/jpeg')
                elif file_path.endswith('.gif'):
                    self.send_header('Content-type', 'image/gif')
                else:
                    self.send_header('Content-type', 'application/octet-stream')
                self.end_headers()
                with open(file_path, 'rb') as file:
                    self.wfile.write(file.read())
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'File not found')

def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    print('Running server on port 8080...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
