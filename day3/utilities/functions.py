from .decorators import timer, logger


@timer
@logger
def add(a, b):
    return a + b


@timer
@logger
def subtract(a, b):
    return a - b


@timer
@logger
def greet(name):
    return f"Hello, {name}!"


def fibonacci_generator(n):
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b