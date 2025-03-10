'''
Question 3
Write a function that returns a function with all arguments, except the first
one, prefilled with certain values provided to the outer function.

(This is sometimes called a partial function).

For example, we may have some functions such as:

import math
def power(x, n):
    return x ** n
def dist(pt1, pt2):
    return math.sqrt(sum(coord_1 - coord_2 for coord_1, coord_2 in
    zip(pt1, pt2)))
Or even functions already defined, such as:

math.gcd(a, b)
or

math.log(x, base)
We want to to be able to generate new functions, based on these ones
(power, dist, gcd, log) but with all the values except the first one prefilled,
for example, assuming our function is named partial, we can use it to define
new functions this way:

squares = partial(power, 2)
dist_from_origin = partial(dist, (0, 0))
gcd_13 = partial(math.gcd, 13)
log_2 = partial(math.log, 2)
log_10 = partial(math.log, 10)
log_16 = partial(math.log, 16)
Then when we call our new functions, we just pass in the value for the first
argument, i.e.

squares(3) --> 9
squares(4) --> 16
dist_from_origin((1, 1)) --> 1.414
log_2(10) --> 3.3219
log_10(10) --> 1.0
log_16(10) --> 0.8304
'''