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

