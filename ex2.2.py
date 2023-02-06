# Assignment 2
# Exerciese 2
# Part 2

import time
import json
import sys

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

file = open("ex2.json")
data = json.load(file)

times = []

print(len(data))

for i in data:
    t1 = time.time()
    func1(i, 0, len(i) - 1)
    t2 = time.time()
    times.append(t2-t1)
        
