
def outer(a, b):
    #print(hex(id(a)))
    sum_ = a + b

    def inner():
        prod = a*b
        print(a, b, sum_, prod)
        return "You just called a closure!"

    return inner

func = outer(2, 3)
print(func)
print(func.__closure__)
print('-'*80)

print(func())
print('-'*80)

def outer(a, b):
    def inner(c):
        return c ** 2
    return inner

func = outer(2, 3)
print(func(10))
print(func.__closure__)
print('-'*80)

def power(n):
    def inner(x):
        return x ** n
    return inner
square = power(2)
print(square)
print(square.__closure__)
print(square(10))

cubes = power(3)
print(cubes.__closure__)
print(cubes(2))
print('-'*80)

def execute(func):
    def inner(a, b):
        result = func(a, b)
        return result
    return inner

def add(a,b):
    return a+b

add_executer = execute(add)
print(add_executer.__closure__)
print(hex(id(add)))
print(add_executer(2, 3))
print('-'*80)

def execute(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return inner

def add(a,b,c):
    print('add...')
    return a+b+c

def say_hello(name, *, formal=True):
    print('say_hello...')
    if formal:
        return f'Pleased to meet you, {name}'
    else:
        return f'Hi, {name}!'

exec_add = execute(add)
execute_greet = execute(say_hello)
print(exec_add(1,2,3))
print(execute_greet('Michael', formal=False))

