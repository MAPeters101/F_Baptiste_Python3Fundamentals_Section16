def add(a, b):
    return a + b

def greet(name):
    return f'Hello, {name}!'

print(add(2,3), greet('John'))

def apply(func, *args):
    result = func(*args)
    return result

print(apply(add, 2, 3))
print(apply(greet, 'John'))
print('-'*80)

print(apply(lambda a, b, c: a+b+c, 10, 20, 30))
print('-'*80)

def mult(a, b):
    return a*b

def power(a, n):
    return a ** n

def choose_operator(name):
    if name == 'add':
        return add
    if name == 'mult':
        return mult
    if name == 'power':
        return power

op = choose_operator('power')
print(op)
print('-'*80)
print(op(2,3))
print('-'*80)


def choose_operator(name):
    def add(a, b):
        return a + b

    def mult(a, b):
        return a*b

    def power(a, n):
        return a ** n

    if name == 'add':
        return add
    if name == 'mult':
        return mult
    if name == 'power':
        return power

op = choose_operator('mult')
print(op(3,4))
print(op)
print('='*80)


def choose_operator(name):
    if name == 'add':
        return lambda a, b: a+b
    if name == 'mult':
        return lambda a, b: a*b
    if name == 'power':
        return lambda a, n: a**n

op = choose_operator('power')
print(op(3,4))
print(op)
#print(op(2,3,4))
print(op)

print('='*80)


