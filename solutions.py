'''
Question 1
We want to write a function that can find an approximate maximum or minimum of some given function over some given range.

For example, given some function:

f(x) = x**2 - 1
our function should return an approximate minimum (or maximum) of f over some given range, say [-5, 5].

We'll do this by essentially splitting our intervals into n points (what I'll call the resolution), evaluating the function at each of these points, and returning either the min or the max.

We want this function to be generic, so it should have the following parameters:

a function of one variable
a range of values defined by start/end values
a value indicating the "resolution"
a value indicating whether we want the min or the max
Solution
Let's start by writing a few single-variable functions:

import math

f1 = lambda x: x ** 2 - 1
f2 = lambda x: abs(x-2)
f3 = lambda x: math.sin(x)
Now let's figure out what parameters we want to define for our function that will determine an approximate min or max:

f: the function used to evaluate approx min/max
start: the left end of the interval - default to -10
end: the right end of the interval - default to 10
resolution: indicates how many times we'll evaluate the function func over the interval [start, end) - default to 1_000
is_min: if True returns the minimum, otherwise returns the maximum - default to True
Let's define the function first, and we'll come back to it's implementation later:

def find_extreme(f, start=-10, end=10, resolution=1_000, is_min=True):
    pass
Our first task will be to calculate the list of values we want to evaluate the function at:

def find_extreme(f, start=-10, end=10, resolution=1_000, is_min=True):
    delta = (end - start) / (resolution - 1)
    data = [start + i * delta for i in range(resolution)]
    return data
find_extreme(None, start=1, end=6, resolution=8)
[1.0,
 1.7142857142857144,
 2.428571428571429,
 3.142857142857143,
 3.857142857142857,
 4.571428571428571,
 5.285714285714286,
 6.0]
Ok, so this is starting to look good. Next we need to evaluate the function at each of those points:

def find_extreme(f, start=-10, end=10, resolution=1_000, is_min=True):
    delta = (end - start) / (resolution - 1)
    data = [start + i * delta for i in range(resolution)]
    f_values = [f(x) for x in data]
    return f_values
find_extreme(f1, -2, 2, 10)
[3.0,
 1.4197530864197532,
 0.23456790123456805,
 -0.5555555555555555,
 -0.9506172839506173,
 -0.9506172839506173,
 -0.5555555555555558,
 0.23456790123456694,
 1.4197530864197523,
 3.0]
Next we'll need to find the minimum of these values:

def find_extreme(f, start=-10, end=10, resolution=1_000, is_min=True):
    delta = (end - start) / (resolution - 1)
    data = [start + i * delta for i in range(resolution)]
    f_values = [f(x) for x in data]
    result = min(f_values)
    return result
find_extreme(f1, -2, 2, 10)
-0.9506172839506173
Of course, the higher our resolution, the better our approximation should be:

find_extreme(f1, -2, 2)
-0.999995991987984
Now let's handle the is_min argument:

def find_extreme(f, start=-10, end=10, resolution=1_000, is_min=True):
    delta = (end - start) / (resolution - 1)
    data = [start + i * delta for i in range(resolution)]
    f_values = [f(x) for x in data]
    if is_min:
        result = min(f_values)
    else:
        result = max(f_values)
    return result
find_extreme(f1, -2, 2), find_extreme(f1, -2, 2, is_min=False)
(-0.999995991987984, 3.0)
And we can try out our other functions too:

find_extreme(f2, -10, 10), find_extreme(f2, -10, 10, is_min=False)
(0.008008008008008716, 12.0)
find_extreme(f3, -10, 10), find_extreme(f3, -10, 10, is_min=False)
(-0.9999996994977832, 0.9999996994977832)
Now let's loook at our function and see if we can simplify our code:

def find_extreme(f, start=-10, end=10, resolution=1_000, is_min=True):
    delta = (end - start) / (resolution - 1)
    data = [start + i * delta for i in range(resolution)]
    f_values = [f(x) for x in data]
    if is_min:
        result = min(f_values)
    else:
        result = max(f_values)
    return result
The first thing to note is that we are creating these lists (data and f_values) - that seems uncessary - we could use generator expressions instead since we will only need to iterate through them once:

def find_extreme(f, start=-10, end=10, resolution=1_000, is_min=True):
    delta = (end - start) / (resolution - 1)
    data = (start + i * delta for i in range(resolution))
    f_values = (f(x) for x in data)
    if is_min:
        result = min(f_values)
    else:
        result = max(f_values)
    return result
find_extreme(f3, -10, 10, is_min=False)
0.9999996994977832
Another thing too, is that we using a comprehension to apply the function func to every value in data - this is fine, but we could also just use the map function:

def find_extreme(f, start=-10, end=10, resolution=1_000, is_min=True):
    delta = (end - start) / (resolution - 1)
    data = (start + i * delta for i in range(resolution))
    f_values = map(f, data)
    if is_min:
        result = min(f_values)
    else:
        result = max(f_values)
    return result
find_extreme(f3, -10, 10, is_min=False)
0.9999996994977832
Additionally, we could use a ternary operator to pick whether we should use min or max:

def find_extreme(f, start=-10, end=10, resolution=1_000, is_min=True):
    delta = (end - start) / (resolution - 1)
    data = (start + i * delta for i in range(resolution))
    f_values = map(f, data)
    min_max = min if is_min else max
    result = min_max(f_values)
    return result
find_extreme(f3, -10, 10), find_extreme(f3, -10, 10, is_min=False)
(-0.9999996994977832, 0.9999996994977832)
And we can then clean up the code this way:

def find_extreme(f, start=-10, end=10, resolution=1_000, is_min=True):
    delta = (end - start) / (resolution - 1)
    data = (start + i * delta for i in range(resolution))
    min_max = min if is_min else max
    return min_max(map(f, data))
find_extreme(f3, -10, 10), find_extreme(f3, -10, 10, is_min=False)
(-0.9999996994977832, 0.9999996994977832)
Question 2
You are given a function of two variables, and a list of tuples containing the values for the two variables.

Create a list that is the result of calling the function on each values in the list, using three different techniques:

a for loop
a list comprehension
the map function
Use the timeit function to time each approach.

Hint: write a function that implements each approach, and then time calling those functions using the timeit function (from timeit import timeit - we've used it before). Also you will want to specify number=10 or something like that when you run timeit - unless you want to sit there watvhing your screen for quite a while :-)

import math

def func(point):
    # expect point to be a sequence of two values
    x, y = point
    return math.hypot(x, y)
    # hypot is a function that calculates sqrt(x**2 + y**2), given a sequence (x, y)

points = [
    (0, 0),
    (1, 1),
    (10, 20),
    (math.pi, math.e)
]
Your result for points should be:

[0.0, 1.4142135623730951, 22.360679774997898, 4.154354402313314]
For timing purposes, use a larger set of points, like this one:

points_large = [(math.sin(x), math.cos(x)) for x in range(1, 1_000_000)]
Solution
A for loop approach could be something like:

results = []
for point in points:
    results.append(func(point))

results
[0.0, 1.4142135623730951, 22.360679774997898, 4.154354402313314]
But whenever we see code that creates an empty list and a loop that just appends to that list with relatively simple code in the loop body, we should consider a comprehension instead.

results = [func(point) for point in points]
results
[0.0, 1.4142135623730951, 22.360679774997898, 4.154354402313314]
But we can also just use the map function:

results = list(map(func, points))
results
[0.0, 1.4142135623730951, 22.360679774997898, 4.154354402313314]
Note: the map function returns a generator, so we pass that to list() to actually generate a list.

Let's write some functions to encapsulate each technique so we can easily use them for timing things:

def calc_loop(f, pts):
    results = []
    for pt in pts:
        results.append(f(pt))
    return results
def calc_comp(f, pts):
    return [f(pt) for pt in pts]
def calc_map(f, pts):
    return list(map(f, pts))
Let's make sure the functions work as expected:

calc_loop(func, points)
[0.0, 1.4142135623730951, 22.360679774997898, 4.154354402313314]
calc_comp(func, points)
[0.0, 1.4142135623730951, 22.360679774997898, 4.154354402313314]
calc_map(func, points)
[0.0, 1.4142135623730951, 22.360679774997898, 4.154354402313314]
Now let's run some timings, using points_large for our arguments:

from timeit import timeit
timeit('calc_loop(func, points_large)', globals=globals(), number=10)
2.010900836
timeit('calc_comp(func, points_large)', globals=globals(), number=10)
1.721283031
timeit('calc_map(func, points_large)', globals=globals(), number=10)
1.5711788810000007
Question 3
Write a function that returns a function with all arguments, except the first one, prefilled with certain values provided to the outer function.

(This is sometimes called a partial function).

For example, we may have some functions such as:

import math
def power(x, n):
    return x ** n
def dist(pt1, pt2):
    return math.sqrt(sum(coord_1 - coord_2 for coord_1, coord_2 in zip(pt1, pt2)))
Or even functions already defined, such as:

math.gcd(a, b)
or

math.log(x, base)
We want to to be able to generate new functions, based on these ones (power, dist, gcd, log) but with all the values except the first one prefilled, for example, assuming our function is named partial, we can use it to define new functions this way:

squares = partial(power, 2)
dist_from_origin = partial(dist, (0, 0))
gcd_13 = partial(math.gcd, 13)
log_2 = partial(math.log, 2)
log_10 = partial(math.log, 10)
log_16 = partial(math.log, 16)
Then when we call our new functions, we just pass in the value for the first argument, i.e.

squares(3) --> 9
squares(4) --> 16
dist_from_origin((1, 1)) --> 1.414
log_2(10) --> 3.3219
log_10(10) --> 1.0
log_16(10) --> 0.8304
Solution
For this we'll use a function that defines and returns a nested function, and captures the function whatever arguments need to be passed to it (aside from the first argument).

def partial(f, *args, **kwargs):
    def inner(first_arg):
        print('func', f.__name__)
        print('first_arg', first_arg)
        print('args', args)
        print('kwargs', kwargs)
    return inner
Let's see how this behaves:

f = partial(power, 2)
This function is a closure, and knows about both power and 2. We can see it this way:

We can call this closure:

f(3)
func power
first_arg 3
args (2,)
kwargs {}
As you can see, the closure captured the power function and the value 2 (in args) - and of course kwargs is empty. If we had a function that requires keyword only arguments, we could pass those in too:

f = partial(lambda x, y, *, k1: (x, y, k1), 10, k1=100)
f(1)
func <lambda>
first_arg 1
args (10,)
kwargs {'k1': 100}
So, we have the basic skeleton for our solution. What we now need to do is actually call the function, inserting first_arg, and return the result of that.

def partial(f, *args, **kwargs):
    def inner(first_arg):
        result = f(first_arg, *args, **kwargs)
        return result
    return inner
We don't actually need to store the result and then return it, we can just return it directly:

def partial(f, *args, **kwargs):
    def inner(first_arg):
        return f(first_arg, *args, **kwargs)
    return inner
Now we can use this to generate some new functions with pre-filled arguments:

squares = partial(power, 2)
dist_from_origin = partial(dist, (0, 0))
gcd_13 = partial(math.gcd, 13)
log_2 = partial(math.log, 2)
log_10 = partial(math.log, 10)
log_16 = partial(math.log, 16)
squares(4)
16
dist_from_origin((1, 1))
1.4142135623730951
gcd_13(169)
13
log_2(10)
3.3219280948873626
log_10(10)
1.0
log_16(10)
0.8304820237218407
Question 4
Write a function that can be used to not only execute another function with specified arguments, but print a "log" (basically just print to the console", of how long it took to execute the function.

For example, given some functions like this:

def norm(x, y):
    return math.sqrt(x**2 + y**2)

def find_index_min(seq):
    min_ = min(seq)
    return seq.index(min_)
Then assuming your logging function is called logged, you could create logged functions this way:

def logged(f):
    # implement this
    pass
norm_logged = logged(norm)
find_index_min_logged = logged(find_index_min)
You would then be able to call norm_logged with some arguments, or find_index_min_logged with some arguments, and not only get the actual result back, but also see an output to the console that tells you how long the function took to run.

Solution
To solve this, we'll use a closure with nested functions.

The outer function will take a single argument, the function f.

def logged(f):
    pass
Then we'll create a nested function that will receive whatever arguments f needs to be called, and we'll return that new inner function (that will be the closure):

def logged(f):
    def inner(*args, **kwargs):
        result = f(*args, **kwargs)
        return result
    return inner
You'll notice that when we call logged(norm) we'll actually get a function back - that inner function whose f value is actually norm - let's try it out:

logged_norm = logged(norm)
logged_norm
<function __main__.logged.<locals>.inner(*args, **kwargs)>
As expected logged_norm is a function - but it is a special function - it knows that f (in it's body) is actually norm.

We can actually see it this way:

logged_norm.__closure__
(<cell at 0x7ff281a01a90: function object at 0x7ff2819ece50>,)
Notice how there is this "cell", which is a function object at some memory address - that memory address is actually the memory address of norm:

hex(id(norm))
'0x7ff2819ece50'
We could also create a logged function for find_index_min:

find_index_min_logged=logged(find_index_min)
find_index_min_logged.__closure__
(<cell at 0x7ff281a01250: function object at 0x7ff2819ecee0>,)
And the function in that closure is actually the find_index_min function:

hex(id(find_index_min))
'0x7ff2819ecee0'
Now let's finish off our logged function - we still need to time things and print that out:

from time import perf_counter

def logged(f):
    def inner(*args, **kwargs):
        start = perf_counter()
        result = f(*args, **kwargs)
        end = perf_counter()
        print(f'elapsed: {end - start} secs')
        return result
    return inner
And let's try it out:

logged_norm = logged(norm)
find_index_min_logged=logged(find_index_min)
result = logged_norm(1, 1)
print(f'result: {result}')
elapsed: 4.817999999850997e-06 secs
result: 1.4142135623730951
result = find_index_min_logged([10, 5, 3, -2, -10, 100])
print(f'result: {result}')
elapsed: 2.6530000001301346e-06 secs
result: 4
'''