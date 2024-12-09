

"""Декоратори:
Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
Напишіть декоратор, який логує аргументи та результати викликаної функції."""


def deco_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f"Exception is {e} in {func}")
    return wrapper



def deco_logger(func):
     def wrapper(*args, **kwargs):
         result = func(*args, **kwargs)
         print(f"Arguments: {args} and {kwargs} return Result: {result}")
         return result
     return wrapper



@deco_exceptions
def add(a, b):
    return a + b

# decorator = deco_logger(add("7"))
func1 = deco_exceptions(add(4, "4"))


@deco_logger
def add(a, b):
    return a + b

# decorator = deco_logger(add("7"))
func2 = deco_logger(add(4, 4))
