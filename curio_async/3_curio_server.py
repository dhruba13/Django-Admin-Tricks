from curio import run, tcp_server

HEADERS = b'HTTP/1.1 200 OK\r\nConnection: close\r\n\r\n'
BODY = '<!DOCTYPE html><html><head><meta charset="utf-8"><title></title></head><body>Hi</body></html>'

async def echo_client(client, addr):
    print('Connection from', addr)
    async with client.as_stream() as stream:
        data = await stream.read()
        if data:
            # print(data, 'Received from', addr)
            ...
        await stream.write(HEADERS)
        await stream.write(BODY.encode('utf-8'))


if __name__ == '__main__':
    run(tcp_server, '', 7070, echo_client)
