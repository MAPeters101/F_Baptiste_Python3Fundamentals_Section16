
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



