from typing import Callable


def memoize(func: Callable) -> Callable:
    """Memoize function"""
    memory = {}

    def wrapper(*args, **kwargs):
        arguments = str(args) + str(kwargs)

        if arguments not in memory:
            memory[arguments] = func(*args, **kwargs)
            return memory[arguments]

        return memory[arguments]

    return wrapper
