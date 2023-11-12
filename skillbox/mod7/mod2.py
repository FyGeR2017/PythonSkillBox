def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    wrapper.__name__ = func.__name__

    return wrapper


@memoize
def fibonacci(n):

    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))  # 5
print(fibonacci(10))  # 55
print(fibonacci(20))  # 6765
print(fibonacci.__name__)  # fibonacci
