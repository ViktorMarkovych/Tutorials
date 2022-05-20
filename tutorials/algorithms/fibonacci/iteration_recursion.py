def fibonacci(n):
    def fibonacci(a, b, n):
        if n < 0:
            return -1
        elif n==0:
            return b
        else:
            return fibonacci(a+b, a, n-1)

    return fibonacci(1, 0, n)