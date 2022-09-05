def fib(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
        quit()

    return fib(num-1) + fib(num-2)

num = int(input())
print(fib(num))
