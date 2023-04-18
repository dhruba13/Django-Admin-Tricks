# asyncio, base_events.py
def default_exception_handler(self, context):
    """Default exception handler. This is called when
    an exception occurs and no exception handler is set """
    ...

    def lines(context):
        for key in context:

            value = context[key]
            ...
            yield '{}: {}'.format(key, value)

    logger.error('\n'.join(lines(context)), exc_info=exc_info)
