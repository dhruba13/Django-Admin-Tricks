    # Synchronous put. For threads.
    def put(self, item):
        while True:
            fut = self._put(item)
            if not fut:
                break
            fut.result()

    gen

    for fut in (self._put(item) for __moment__)


    gen = (await self.requests.get() for __moment_ in infinity)
    for coro in (coro for coro in gen if coro or gen.close()):
        await coro

# requests utils.py ~ row 831
def select_proxy(url, proxies):
    """Select a proxy for the url, if applicable."""

    proxy = None
    for proxy_key in proxy_keys:
        if proxy_key in proxies:
            proxy = proxies[proxy_key]
            break
    return proxy

def select_proxy(url, proxies):
    """Select a proxy for the url, if applicable."""
    ...
    proxy_gen = (proxies[key] for key in proxy_keys if key in proxies)
    return next(proxy_gen, None)


    if isinstance(obj, (list, set, frozenset, GeneratorType, tuple)):
        return (jsonable_encoder(
                    item,
                    include=include,
                    exclude=exclude,
                    by_alias=by_alias,
                    exclude_unset=exclude_unset,
                    exclude_defaults=exclude_defaults,
                    exclude_none=exclude_none,
                    custom_encoder=custom_encoder,
                    sqlalchemy_safe=sqlalchemy_safe,
                ) for item in obj)
