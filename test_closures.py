from .closures import *

## TEST CLOSURE 1
def test_fn_with_gte_50_doc_string():
    """
    This is a function with a doc string, and the doc string is 50 char long
    """
    pass

def test_fn_with_lte_50_doc_string():
    """
    This fn has docstring, but lte 50 char
    """
    pass  

print(has_lengthy_docstring(test_fn_with_gte_50_doc_string)())
print(has_lengthy_docstring(test_fn_with_lte_50_doc_string)())
c = has_lengthy_docstring(test_fn_with_gte_50_doc_string)
print(c.__closure__)


## TEST CLOSURE 2
next_fib = generate_next_fib_num()

for _ in range(10):
    print(next_fib())


## TEST CLOSURE 3
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

add = track_fn_call_counts(add)
mul = track_fn_call_counts(mul)
div = track_fn_call_counts(div)
print("Before any fn calls : ", counters)
add(1, 2)
add(3, 5)
mul(1, 2)
div(2, 4)
print("After fn calls : ", counters)