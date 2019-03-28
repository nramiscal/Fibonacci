fibonacci_cache = {}

def fibonacci(n):

    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n < 2:
        value = n
    else:
        value = fibonacci(n-1) + fibonacci(n-2)

    fibonacci_cache[n] = value
    return value

for n in range(1,1001):
    print(n, ":", fibonacci(n))
