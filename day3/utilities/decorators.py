import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print(f"{func.__name__} took {end_time - start_time:.6f} seconds")

        return result

    return wrapper


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}")

        result = func(*args, **kwargs)

        print(f"Function {func.__name__} completed")

        return result

    return wrapper