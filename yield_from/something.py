starlette
datastructires.py row ~38

host_header = None
for key, value in scope["headers"]:
    if key == b"host":
        host_header = value.decode("latin-1")
        break

host_header = next((val.decode("latin-1") for key, val in scope["headers"] if key == b"host"), None)
