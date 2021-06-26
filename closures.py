## CLOSURE 1
def has_lengthy_docstring(fn):
    """
    A closure that takes a function and then check whether the function passed 
    has a docstring with more than 50 characters. 50 is stored as a free variable.

    Arguments:
        fn: a function for which the doc string length will be validated to be 50
    Returns:
        bool value, if True meets docstring criterion
    """
    min_doc_string_length = 50
    def inner():
        return len(fn.__doc__) >= min_doc_string_length
    return inner


def generate_next_fib_num():
    """
    A closure that gives you the next Fibonacci number.
    """
    prev = 0
    next = 1
    def inner():
        nonlocal prev, next
        prev, next = next, prev + next
        return prev
    return inner


counters = dict()

def track_fn_call_counts(fn):
    """
    A Closuer that can keep a track of how many times add/mul/div functions were 
    called, and update a global dictionary variable with the counts.
    """
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        counters[fn.__name__] = count
        return fn(*args, **kwargs)
    return inner


