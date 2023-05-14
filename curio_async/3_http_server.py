from http.server import HTTPServer, BaseHTTPRequestHandler

HEADERS = b'HTTP/1.1 200 OK\r\nConnection: close\r\n\r\n'
BODY = '<!DOCTYPE html><html><head><meta charset="utf-8"><title></title></head><body>Hi</body></html>'

class echo_client(BaseHTTPRequestHandler):

    def do_GET(self):
        print('Connection from', self.client_address)
        data = self.requestline
        stream = self.wfile
        stream.write(HEADERS)
        stream.write(BODY.encode('utf-8'))

if __name__ == '__main__':
    HTTPServer(('', 9090), echo_client).serve_forever()
