# cgpy
things that I use a lot in python

**lets**

*Lets allows you to create a scope to do some work and keep the result, or simply use it for side effects without littering your current scope's namespace*
```
from lets import let
from lets import letAs
from lets import mapAs
from lets import returnAs

x = 1
y = 2
z = 3

@let
def a():
    x = 100
    y = 200
    z = 300
    return x + y + z
    
print(x, y, z, a)
# > 1 2 3 600

@letAs(list)
def b():
    x = 100
    y = 200
    z = 300
    yield x
    yield x + y
    yield x + y + z

print(x, y, z, b)
# > 1 2 3 [100, 300, 600]

@returnAs(''.join)
def c(show_b=True):
    yield 'a'
    if show_b:
        yield 'b'
    yield 'c'
    
print(c())
# > 'abc'
print(c(show_b=False))
# > 'ac'

@letAs('<ol>{}</ol>'.format)
@letAs(''.join)
@mapAs('<li>{}</li>'.format)
def d():
    yield 'a'
    yield 'b'
    yield 'c'
```

