def currency(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'{result} руб.'
    return wrapper


def price_calculation(price, tax):
    return price * (1 + tax)


price_calculation = currency(price_calculation)
print(price_calculation(100, 0.05))
