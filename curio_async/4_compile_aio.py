from aiohttp.web import Application, run_app, StreamResponse, Response

BODY_START = '<!DOCTYPE html><html><head><meta charset="utf-8"><title></title></head><body>'
BODY_END = '</body></html>'

import asyncio
import time
import aiofiles
import hashlib

from europython2023.curio_async import FILE_LIST, REPORT
from europython2023.curio_async import REPORT as print


async def render(data, idx):
    print('render start', idx)
    text = data.decode('utf-8')
    sha1 = hashlib.sha1(data)  # .update(data)
    text = f'<h1>File: {idx}</h1><pre><code>{text}</code></pre><p>Sha1: <samp>{sha1.hexdigest()}</samp><p>'.encode('utf-8')
    print('rendered', idx)
    return text, idx


async def read(filename, idx):
    print('started', filename, idx)
    async with aiofiles.open(f'{filename}', mode='rb') as file:
        try:
            return (await file.read(), idx)
        finally:
            print('readed', filename, idx)


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
    await stream.write(BODY_START.encode('utf-8'))

    tasks = []
    for idx, filename in enumerate(FILE_LIST):
        tasks.append(asyncio.create_task(read(filename, idx)))

    response = await asyncio.gather(*tasks, return_exceptions=True)

    tasks = []
    for result in response:
        tasks.append(asyncio.create_task(render(*result)))

    response = await asyncio.gather(*tasks, return_exceptions=True)

    tasks = []
    for text, idx in response:
        tasks.append(asyncio.create_task(stream.write(text)))

    response = await asyncio.gather(*tasks, return_exceptions=True)

    await stream.write(BODY_END.encode('utf-8'))
    await stream.write_eof()

if __name__ == '__main__':
    app = Application()
    app.router.add_route('GET', '/', echo_client)
    run_app(app)
