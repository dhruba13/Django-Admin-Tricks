from aiohttp.web import Response, Application, run_app, StreamResponse

HEADERS = b'HTTP/1.1 200 OK\r\nContent-type: text/html\r\nConnection: close\r\n\r\n'
BODY = '<!DOCTYPE html><html><head><meta charset="utf-8"><title></title></head><body>Hi</body></html>'


async def echo_client(request):
    return Response(body=BODY, content_type = 'text/html', charset = 'utf-8')

if __name__ == '__main__':
    app = Application()
    app.router.add_route('GET', '/', echo_client)
    run_app(app)
