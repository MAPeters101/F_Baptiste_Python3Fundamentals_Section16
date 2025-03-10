'''
Question 1
We want to write a function that can find an approximate maximum or minimum of
some given function over some given range.

For example, given some function:

f(x) = x**2 - 1
our function should return an approximate minimum (or maximum) of f over some
given range, say [-5, 5].

We'll do this by essentially splitting our intervals into n points (what I'll
call the resolution), evaluating the function at each of these points, and
returning either the min or the max.

We want this function to be generic, so it should have the following
parameters:

a function of one variable
a range of values defined by start/end values
a value indicating the "resolution"
a value indicating whether we want the min or the max
'''