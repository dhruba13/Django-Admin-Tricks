def get_openapi_operation_parameters(all_route_params, *ag, **kw):
    for param in all_route_params:
        field_info = param.field_info
        if not field_info.include_in_schema:
            continue
        ...  # some staff


def get_openapi_operation_parameters(*args, **kwargs):
    gen = ((param, param.field_info) for param in all_route_params)
    for param, field_info in ((param, info) for param, info in all_route_params if info.include_in_schema):
        ...  # some staff


def build_values(self, *args, **kwargs):
    arg_iter = enumerate(args)
    ...
    while True:
        try:
            i, a = next(arg_iter)
        except StopIteration:
            break
        arg_name = self.arg_mapping.get(i)
        # do something


def build_values(self, *args, **kwargs):
    arg_iter = enumerate(args)
    ...
    func = self.arg_mapping.get
    gen = (func(idx), arg for idx, arg in arg_iter)
    for arg_name, arg in gen:
        # do something