'''
Each recurisve call creates its own scope and environment.
Binding of variables are not changed by recursive call.

'''

#Implementation of Fibonaaci Series
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))
print(fib(7))
print(fib(9))
#fib(50) does not work. Because the number of recursive calls have exceeded. In other words, time limit has exceeded
#print(fib(50))

#Solution is Memoization
memo = {}
def fib_2(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    value = fib_2(n-1) + fib_2(n-2)
    memo[n] = value
    return value

print(fib_2(1000))

#Memoization using built in lru_cache module from functools
from functools import lru_cache

#maxsize specifies number of values o cache, default value of maxsize is 128
@lru_cache(maxsize=1000)
def fib_3(n):
    if type(n) != int:
        raise TypeError('N must be of type int')
    if n < 0:
        raise ValueError('N Must be positive int')
    if n <= 1:
        return n
    return fib_3(n-1) + fib_3(n-2)

fib_3(1000)
#fib('Rabi')
#fib(-1)
