
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
print('-'*80)

def factorial(n):
    prod = 1
    for i in range(2, n+1):
        prod *= i
    return prod

def diagonal_matrix(rows, cols, *, diagonal=1):
    return [
        [
            diagonal if row == col else 0
            for col in range(cols)
        ]
        for row in range(rows)
    ]

print(factorial(4))
print(diagonal_matrix(3, 4, diagonal=-10))
print('-'*80)

from time import perf_counter
import sys
from pprint import pprint

sys.set_int_max_str_digits(100_000)
start = perf_counter()
result = factorial(10_000)
end = perf_counter()
print(f'elapsed: {end - start}')
print(f'result = {result}')
print('-'*80)

start = perf_counter()
result = diagonal_matrix(10, 10, diagonal=-1)
end = perf_counter()
print(f'elapsed: {end - start}')
print(f'result = {result}')
print('-'*80)

def time_it(func, *args, **kwargs):
    start = perf_counter()
    result = func(*args, **kwargs)
    end = perf_counter()
    print(f'elapsed: {end - start}')
    return result

result = time_it(factorial, 10_000)
print(result)
print('-'*80)

result = time_it(diagonal_matrix, 10, 10, diagonal=-1)
print(result)
pprint(result)

print('-'*80)


