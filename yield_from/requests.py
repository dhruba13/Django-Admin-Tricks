def remove_cookie_by_name(cookiejar, name, domain=None, path=None):
    """Unsets a cookie by name, by default over all domains and paths.

    Wraps CookieJar.clear(), is O(n).
    """
    clearables = []
    for cookie in cookiejar:
        if cookie.name == name:
            continue
        if domain is not None and domain != cookie.domain:
            continue
        if path is not None and path != cookie.path:
            continue
        clearables.append(cookie)
    return clearables


def remove_cookie_by_name_gen(cookiejar, name, domain=None, path=None):
    """Unsets a cookie by name, by default over all domains and paths """

    clearables = (cookie for cookie in cookiejar if cookie.name != name)
    if domain is not None:
        clearables = (cookie for cookie in clearables if domain == cookie.domain)
    if path is not None:
        clearables = (cookie for cookie in clearables if path == cookie.path)
    return clearables


from time import perf_counter_ns
from collections import namedtuple
from random import choice
from string import ascii_uppercase, digits

def random_string(size=6):
    return ''.join(choice(ascii_uppercase + digits) for _ in range(size))

def check(count=10, domain=None, path=None):
    Cookie = namedtuple('Cookie', ['name', 'domain', 'path'], defaults=[None, None])
    name = random_string()
    cookie = Cookie(name)
    cookie1 = Cookie(f'{name}1')
    cookie2 = Cookie(name, domain)
    cookie3 = Cookie(f'{name}1', domain)
    cookie4 = Cookie(f'{name}1', f'{domain}1')
    cookie5 = Cookie(name, path=path)
    cookie6 = Cookie(f'{name}1', path=f'{path}1')
    cookie7 = Cookie(name, domain, path)
    cookie8 = Cookie(f'{name}1', f'{domain}1', f'{path}1')
    cookie9 = Cookie(f'{name}1', domain, path)
    cookies = [cookie, cookie1, cookie2, cookie3, cookie4, cookie5, cookie6, cookie7, cookie8, cookie9] * (10 ** count)

    counted = len(cookies)

    time = perf_counter_ns()
    for clearable in remove_cookie_by_name(cookies, name, domain, path):
        # print(clearable)
        clearable = clearable
    listed = (perf_counter_ns()-time)

    time = perf_counter_ns()
    for clearable in remove_cookie_by_name_gen(cookies, name, domain, path):
        # print(clearable)
        clearable = clearable
    generated = (perf_counter_ns()-time)

    print(count, counted, listed, generated, listed - generated)

for i in range(6):
    domain = random_string()
    path = random_string()
    check(i, None, path)
