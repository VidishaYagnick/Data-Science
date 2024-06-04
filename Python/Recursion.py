def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)
    
print(fact(5))

#PRINT FIRST N NUMBERS OF FIBONNACI SERIES


def fibonacci(n):

    # base cases :
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    
    fib_series = fibonacci(n - 1)
    next_number = fib_series[-1] + fib_series[-2]
    fib_series.append(next_number)
    return fib_series
    
print(fibonacci(4))