def julia_fib(n):
    if n<2:
        return n
    return julia_fib(n-1)+julia_fib(n-2)