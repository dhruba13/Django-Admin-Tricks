import hashlib
from http.server import HTTPServer, BaseHTTPRequestHandler
from europython2023.curio_async import FILE_LIST, REPORT as print


HEADERS = b'HTTP/1.1 200 OK\r\nContent-type: text/html; charset=utf-8\r\nConnection: close\r\n\r\n'
BODY_START = '<!DOCTYPE html><html><head><meta charset="utf-8"><title></title></head><body>'
BODY_END = '</body></html>'



def render(data, idx):
    print('render start', idx)
    text = data.decode('utf-8')
    sha1 = hashlib.sha1(data)  # .update(data)
    text = f'<h1>File: {idx}</h1><pre><code>{text}</code></pre><p>Sha1: <samp>{sha1.hexdigest()}</samp><p>'.encode('utf-8')
    print('rendered', idx)
    return text, idx


def read(filename, idx):
    print('started', filename, idx)
    with open(filename, 'rb') as file:
        try:
            return (file.read(), idx)
        finally:
            print('readed', filename, idx)


class echo_client(BaseHTTPRequestHandler):

    def do_GET(self):
        print('Connection from', self.client_address)
        data = self.requestline
        if data:
            # print(data, 'Received from', addr)
            ...
        stream = self.wfile
        stream.write(HEADERS)
        stream.write(BODY_START.encode('utf-8'))

        tasks = []

        for idx, filename in enumerate(FILE_LIST):
            tasks.append(read(f'{filename}', idx))

        print('read completed.')

        renderers = []
        for result in tasks:
            renderers.append(render(*result))

        print('render completed.')

        for rendered, idx in renderers:
            stream.write(rendered)


        stream.write(BODY_END.encode('utf-8'))


if __name__ == '__main__':
    HTTPServer(('', 9090), echo_client).serve_forever()
