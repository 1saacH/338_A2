#timing stuff

import timeit, functools
import matplotlib.pyplot as plt

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

prev_calcs = {}

def fib_mem(n):
    if n in prev_calcs:
        return prev_calcs[n]
    elif n <= 1:
        calced = n
    else:
        calced = fib_mem(n - 1) + fib_mem (n - 2)
    prev_calcs[n] = calced
    return calced

if __name__ == "__main__":

    slow_times = []
    fast_times = []

    for i in range (35):
        t = timeit.Timer(functools.partial(func, i))
        slow_times.append(t.timeit(5))

    for j in range (35):
        k = timeit.Timer(functools.partial(fib_mem, j))
        fast_times.append(k.timeit(5))
    
    plt.plot(slow_times, label="Given Algorithm")
    plt.plot(fast_times, label="Improved Algorithm")

    plt.legend(loc="upper left")
    plt.xlabel("Input")
    plt.ylabel("Seconds")

    plt.show()