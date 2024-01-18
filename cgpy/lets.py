from functools import partial


def let(fn):
    """
    Return the execution of the decorated function, the wrapped function must
    take no arguments
    """
    return fn()


def letAs(constructor, *args, **kwargs):
    """
    Return the execution of the decorated function passed to a constructor.
    Optionally args and kwargs can be passed to the constructor to support
    functions like sorted and filter
    """

    def decorator(fn):
        return constructor(*args, fn() if callable(fn) else fn, **kwargs)

    return decorator


def mapAs(constructor, **kwargs):
    partialContructor = partial(constructor, **kwargs)
    return lambda obj: map(partialContructor, obj() if callable(obj) else obj)


def returnAs(constructor, *a, **kw):
    def wrapper(fn):
        def wrapped(*args, **kwargs):
            return constructor(*a, fn(*args, **kwargs), **kw)

        return wrapped

    return wrapper


if __name__ == "__main__":
    print("testing")

    @returnAs(list)
    def lst():
        yield 1
        yield 2

    assert lst() == [1, 2]

    @returnAs(list)
    @returnAs(filter, None)
    def lst():
        yield 1
        yield None
        yield 2

    assert lst() == [1, 2]

    @returnAs(sorted, key=str.lower)
    def lst():
        yield "b"
        yield "A"
        yield "aa"
        yield "BB"

    assert lst() == ["A", "aa", "b", "BB"]

    @let
    def lst():
        return [1, 2]

    assert lst == [1, 2]

    @letAs(list)
    def lst():
        yield 1
        yield 2

    assert lst == [1, 2]

    @letAs(list)
    @letAs(map, str.lower)
    def lst():
        yield "A"
        yield "B"
        yield "C"

    assert lst == ["a", "b", "c"], lst
