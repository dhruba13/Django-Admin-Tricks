
    def get_readonly_fields(self, request, obj=None):
        response = super().get_readonly_fields(request, obj)
        if not request.user.is_superuser:
            read_only_fields += 'request_status',
        return read_only_fields


    def get_readonly_fields(self, request, obj=None):
        yield from super().get_readonly_fields(request, obj)
        if not request.user.is_superuser:
            yield 'request_status',
