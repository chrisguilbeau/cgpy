# cgpy
things that I use a lot in python

to install: `pip3 install git+https://github.com/chrisguilbeau/cgpy`

**lets**

*Lets allows you to create a scope to do some work and keep the result, or simply use it for side effects without littering your current scope's namespace*
```
from cgpy.lets import let
from cgpy.lets import letAs
from cgpy.lets import mapAs
from cgpy.lets import returnAs

x = 1
y = 2
z = 3

@let
def a():
    x = 100 # only changes x inside this scope
    y = 200
    z = 300
    return x + y + z

# at this point the scope from the above method is gone from memory
# the result is stored in a variable with the name of the method
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

# can be used as as a pipeline as well
@letAs('<ol>{}</ol>'.format)
@letAs(''.join)
@mapAs('<li>{}</li>'.format)
def d():
    yield 'a'
    yield 'b'
    yield 'c'
```

