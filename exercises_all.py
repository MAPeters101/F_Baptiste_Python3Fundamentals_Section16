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
'''