python -m cProfile -o 1_async.pstat 1_async.py sleep 3 sec 1.02334
python -m cProfile -o 1_curi.pstat 1_curi.py sleep 3 sec 1.0183
python -m cProfile -o 1_tri.pstat 1_tri.py sleep 3 sec  1.10381

python -m cProfile -o 2_syncfile.pstat 2_syncfile.py read 4 files  - 0.17791
python -m cProfile -o 2_aiofile.pstat 2_aiofile.py read 4 files - 0.09402
python -m cProfile -o 2_curiofile.pstat 2_curiofile.py curio read 4 files - 0.19922


python 3_curio_server.py curio echo http server


