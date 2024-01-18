from collections.abc import Iterable
from functools import partial


def flatten(_list):
    for item in _list:
        if isinstance(item, Iterable) and not isinstance(item, str):
            for subItem in flatten(item):
                yield subItem
        else:
            yield item


def getAttrText(_attr, value):
    attr = _attr.strip('_')
    if value is True:
        result = attr
    elif value in (False, None):
        result = ""
    else:
        result = "{}='{}'".format(attr, value)
    return result

def _tagAttrs(**kwargs):
    return " " + " ".join(getAttrText(k, v) for k, v in kwargs.items())


def _tagContent(*args):
    return "".join(flatten(args))


def _tag(_name, *args, **kwargs):
    return "<{_name}{attrs}>{content}</{_name}>".format(
        _name=_name,
        attrs=_tagAttrs(**kwargs) if kwargs else "",
        content=_tagContent(*args),
        )


class TagMeta(object.__class__):
    def __getattribute__(self, attr):
        return (
            _tagContent if attr == '_' else
            partial(_tag, attr)
            )


class t(metaclass=TagMeta):
    pass
