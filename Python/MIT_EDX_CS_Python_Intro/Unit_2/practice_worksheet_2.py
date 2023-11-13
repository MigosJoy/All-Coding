# Practice Exercises for functions and scope - 11/2

def a(x):
    '''
    x: int or float.
    '''
    return x+1


def b(x):
    '''
    x: int or float.
    '''
    return x+1.0

# a(a(a(6)))


def c(x, y):
    '''
    x: int or float 
    y: int or float 
    '''
    return x+y


def d(x, y):
    '''
    x: can be of any type
    y: can be of any type
    '''
    return x > y


def e(x, y, z):
    '''
    x: can be of any type
    y: can be of any type
    z: can be of any type
    '''
    return x >= y and x <= z


def f(x, y):
    '''
    x: int or float.
    y: int or float
    '''
    x + y - 2

# c(a(1),b(1))

# d('apple', 11.1)
# e(a(3),b(4),c(3,4))


f
