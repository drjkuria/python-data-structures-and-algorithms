"""Generating Fibonacci sequence using iteration
and recursion.
The Fibonacci Sequence follows one rule: get the next number in the
sequence by adding the previous two numbers, e.g.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ..."""


def get_fib_iterative(position):
    """Get nth position fibonacci number iteratively."""
    first = 0
    second = 1
    next_fib = first + second
    if position == 0:
        return first
    elif position == 1:
        return second
    else:
        for i in  range(2, position):
            first = second
            second = next_fib
            next_fib = first + second
    return next_fib

def get_fib_recursive(position):
    """Get nth postion fibonacci number recursively."""
    first = 0
    second = 1
    next_fib = first + second
    if position == 0:
        return first
    elif position == 1:
        return second
    else:
        return get_fib_recursive(position - 1) + get_fib_recursive(position - 2)
