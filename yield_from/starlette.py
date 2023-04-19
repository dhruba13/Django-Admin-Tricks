    def _read_file(self, file_name: typing.Union[str, Path]) -> typing.Dict[str, str]:
        file_values: typing.Dict[str, str] = {}
        with open(file_name) as input_file:
            for line in input_file.readlines():
                line = line.strip()
                if "=" in line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip().strip("\"'")
                    file_values[key] = value
        return file_values

# starlette config.py

def _read_file(self, file_name):
    file_values = {}
    with open(file_name) as input_file:
        for line in input_file.readlines():
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip().strip("\"'")
                file_values[key] = value
    return file_values


def _read_file(self, file_name):
    with open(file_name) as input_file:
        lines = (line for line in input_file.readline())
        lines = (line.strip() for line in lines if line or lines.close())
        lines = (line.partition("=") for line in lines if not line.startswith("#"))
        return {key.rstrip() : value.lstrip().strip("\"'")
                    for key, separator, val in lines if separator}

