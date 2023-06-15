# VARIABLE SCOPE
# LEGB: Local, Enclosing, Global, Built-in

# Global
x = 'global x'

def test():
    global x # set global variable in the local scope of a function, not used often
    x = 'local x'
    print(x)

# Local
def test():
    y = 'local y'
    print(y)

# Built-in
# built-ins can be overridden so be careful
import builtins
print(dir(builtins)) # gets list of builtin variables

# Enclosing
# Variables can be accessed from scope of functions inside of function, however local takes priority
def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()


def outer():
    x = 'outer x'

    def inner():
        nonlocal x # useful to change the state of closures and decorators
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()