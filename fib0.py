#Automatic memoization (remember past function results)
import functools
@functools.lru_cache(maxsize=None)

def fib0(n):
    if n==0:
        return n
    if n==1:
        return n
    return fib0(n-1) + fib0(n-2)

if __name__ == "__main__":
    print(fib0(10))