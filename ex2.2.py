# Assignment 2
# Exerciese 2
# Part 2

import timeit, functools, json, sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


if __name__ == "__main__":

    file = open("ex2.json")
    data = json.load(file)    

    times = []

    for i in data:
        t = timeit.Timer(functools.partial(func2, i, 0, len(i)-1))
        times.append(t.timeit(5))
    
    plt.plot(times)
    
    plt.xlabel("Input")
    plt.ylabel("Seconds")

    plt.show()
        
