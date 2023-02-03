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



if __name__ == "main":
    index = int(input("Index: "))
    print(fib_mem(index))