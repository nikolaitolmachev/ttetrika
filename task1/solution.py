from functools import wraps


def strict(func):
    annotations = func.__annotations__
    arg_names = [name for name in annotations if name != 'return']

    @wraps(func)
    def wrapper(*args, **kwargs):

        for i in range(len(args)):
            expected_type = annotations[arg_names[i]]
            if not isinstance(args[i], expected_type):
                raise TypeError(f'Wrong expexted type for "{arg_names[i]}"!')

        for name, value in kwargs.items():
            if name in annotations:
                expected_type = annotations[name]
                if not isinstance(value, expected_type):
                    raise TypeError(f'Wrong expexted type for "{name}"!')

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


#print(sum_two(1, 2))  # >>> 3
#print(sum_two(1, 2.4))  # >>> TypeError
