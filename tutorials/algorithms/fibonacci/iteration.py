FIBONACCI = [0, 1, 1]

def fibonacci(n: int) -> int:
    fibonacci_cache = FIBONACCI.copy()
    if n < 0:
        return -1
    elif n < 3:
        return fibonacci_cache[n]
    elif n >= 3:
        for i in range(3, n + 1):
            fibonacci_cache.append(fibonacci_cache[i - 1] + fibonacci_cache[i - 2])
    return fibonacci_cache[n]