from typing import Callable

cache_res = dict()


def cache(func: Callable) -> Callable:
    def wrapper(x):
        key = (x, func)
        if key in cache_res:
            return cache_res[key]
        res = func(x)
        cache_res[key] = res
        return cache_res[key]

    return wrapper
