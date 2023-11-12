def validate_args(func):
    def wrapper(*args):
        if len(args) < 1:
            return "Not enough arguments"
        elif len(args) > 1:
            return "Too many arguments"
        elif not isinstance(args[0], int):
            return "Wrong types"
        elif args[0] < 0:
            return "Negative argument"
        else:
            return func(*args)
    return wrapper


@validate_args
def calculate_square(num):
    return num ** 2


print(calculate_square(5))  # 25
print(calculate_square())   # Not enough arguments
print(calculate_square(5, 6))  # Too many arguments
print(calculate_square("hello"))  # Wrong types
print(calculate_square(-2))  # Negative argument
