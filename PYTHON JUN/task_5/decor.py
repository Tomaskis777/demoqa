# def currency(fn):
#     def wrapper(*args, **kwargs):
#         result = fn(*args, **kwargs)
#         print(fn.__name__)
#         return f'{result} руб.'
#     return wrapper
#
#
# @currency
# def price_calculation(price, tax):
#     return price * (1 + tax)
#
#
# # price_calculation = currency(price_calculation)
# print(price_calculation(100, 0.05))


def print_result(f):
    def result(x):
        r = f(x)
        print(f'Результат выислений: {r}')
        return r
    return result


@print_result
def square(x):
    return x ** 2


@print_result
def multiply(x):
    return x * 2


square(3)
multiply(3)
