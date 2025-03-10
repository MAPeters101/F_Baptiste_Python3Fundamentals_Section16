'''
Question 4
Write a function that can be used to not only execute another function with
specified arguments, but print a "log" (basically just print to the console",
of how long it took to execute the function.

For example, given some functions like this:

def norm(x, y):
    return math.sqrt(x**2 + y**2)

def find_index_min(seq):
    min_ = min(seq)
    return seq.index(min_)
Then assuming your logging function is called logged, you could create logged
functions this way:

def logged(f):
    # implement this
    pass
norm_logged = logged(norm)
find_index_min_logged = logged(find_index_min)
You would then be able to call norm_logged with some arguments, or
find_index_min_logged with some arguments, and not only get the actual result
back, but also see an output to the console that tells you how long the
function took to run.
'''