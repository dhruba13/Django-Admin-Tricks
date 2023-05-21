import curio
import hashlib
from curio import run, tcp_server

from europython2023.curio_async import REPORT, FILE_LIST
from europython2023.curio_async import REPORT as print

HEADERS = b'HTTP/1.1 200 OK\r\nContent-type: text/html; charset=utf-8\r\nConnection: close\r\n\r\n'
BODY_START = '<!DOCTYPE html><html><head><meta charset="utf-8"><title></title></head><body>'
BODY_END = '</body></html>'



async def read(filename, idx):
    # print(f'One {filename}')
    print('started', filename, idx)
    async with curio.file.aopen(filename, 'rb') as file:
        try:
            return (await file.read(), idx)
        finally:
            print('readed', filename, idx)


async def render(data, idx):
    print('render start', idx)
    text = data.decode('utf-8')
    sha1 = hashlib.sha1(data)  # .update(data)
    text = f'<h1>File: {idx}</h1><pre><code>{text}</code></pre><p>Sha1: <samp>{sha1.hexdigest()}</samp><p>'.encode('utf-8')
    print('rendered', idx)
    return text, idx


async def processing(stream, filename, idx):
    readed, *_ = await read(filename, idx)
    rendered, *_ = await render(readed, idx)
    await stream.write(rendered)


async def echo_client(client, addr):
    print('Connection from', addr)
    async with client.as_stream() as stream:
        data = await stream.read()
        if data:
            print(data, 'Received from', addr)

        await stream.write(HEADERS)
        await stream.write(BODY_START.encode('utf-8'))

        async with curio.TaskGroup() as reads:
            for idx, filename in enumerate(FILE_LIST):
                await reads.spawn(processing, stream, f'{filename}', idx)


        await stream.write(BODY_END.encode('utf-8'))

if __name__ == '__main__':
    run(tcp_server, '', 7070, echo_client)
