from functools import partial

def let(fn):
    return fn()

def letAs(constructor, **kwargs):
    return lambda fn: constructor(
        fn() if callable(fn) else fn, **kwargs)

def mapAs(constructor, **kwargs):
    partialContructor = partial(constructor, **kwargs)
    return lambda obj: map(
        partialContructor, obj() if callable(obj) else obj)

def returnAs(constructor, **kw):
    def wrapper(fn):
        def wrapped(*args, **kwargs):
            return constructor(fn(*args, **kwargs), **kw)
        return wrapped
    return wrapper
