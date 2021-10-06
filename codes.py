from lets import returnAs
from tags import t
from json import dumps as json_encode # noqa
from json import loads as json_decode # noqa

JSON_KEY = '_json_'

@returnAs(''.join)
def page(content):
    yield '<!DOCTYPE html>'
    yield t.html(
        t.head(
            t.link(rel='stylesheet', href='/static/flex.css'),
            t.link(rel='stylesheet', href='/static/style.css'),
            t.script(src='/static/jquery.js'),
            t.script(src='/static/script.js'),
            ),
        t.body(content),
        )
