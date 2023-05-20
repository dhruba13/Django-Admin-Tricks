from aiohttp.web import Application, run_app, StreamResponse, Response

# HEADERS = b'HTTP/1.1 200 OK\r\nContent-type: text/html; charset=utf-8\r\nConnection: close\r\n\r\n'
BODY = '<!DOCTYPE html><html><head><meta charset="utf-8"><title></title></head><body>Hi</body></html>'


async def echo_client(request):
    print('Connection from', request.transport.get_extra_info('socket').getpeername()[1])
    data = await request.read()
    if data:
        # print(data, 'Received from', addr)
        ...
    stream = StreamResponse()
    stream.content_type = 'text/html'
    stream.charset= 'utf-8'
    await stream.prepare(request)
    #await stream.write(HEADERS)
    await stream.write(BODY.encode('utf-8'))
    await stream.write_eof()

if __name__ == '__main__':
    app = Application()
    app.router.add_route('GET', '/', echo_client)
    run_app(app)
