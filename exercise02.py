'''
Question 2
You are given a function of two variables, and a list of tuples containing the
values for the two variables.

Create a list that is the result of calling the function on each values in the
list, using three different techniques:

a for loop
a list comprehension
the map function
Use the timeit function to time each approach.

Hint: write a function that implements each approach, and then time calling
those functions using the timeit function (from timeit import timeit - we've
used it before). Also you will want to specify number=10 or something like
that when you run timeit - unless you want to sit there watvhing your screen
for quite a while :-)

import math

def func(point):
    # expect point to be a sequence of two values
    x, y = point
    return math.hypot(x, y)
    # hypot is a function that calculates sqrt(x**2 + y**2), given a sequence
    (x, y)

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
'''