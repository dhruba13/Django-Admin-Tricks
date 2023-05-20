python -m cProfile -o pstat/1_async.pstat 1_async.py sleep 3 sec 1.02334
python -m cProfile -o pstat/1_curi.pstat 1_curi.py sleep 3 sec 1.0183
python -m cProfile -o pstat/1_tri.pstat 1_tri.py sleep 3 sec  1.10381
python -m cProfile -o pstat/2_syncfile.pstat 2_syncfile.py read 4 files  - 0.21873
python -m cProfile -o pstat/2_aiofile.pstat 2_aiofile
.py read 4 files - 0.05405
python -m cProfile -o pstat/2_curiofile.pstat 2_curiofile.py curio read 4 files - 0.03910


python 3_curio_server.py curio echo http server
hey http://127.0.0.1:7070/ -z 15s -c 1 -n 100       

python 3_aiohttp_server.py
hey http://127.0.0.1:8080/ -z 15s -c 1 -n 100

python 3_http_server.py
hey http://127.0.0.1:9090/ -z 15s -c 1 -n 100




python 4_final.py curio read and render http server
hey http://127.0.0.1:7070/ -z 15s -c 1 -n 100