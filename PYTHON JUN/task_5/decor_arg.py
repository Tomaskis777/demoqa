def currency(currency_name):
    def decor(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            print(fn.__name__)
            return f'{result} {currency_name}'
        return wrapper
    return decor


@currency('$')
def price_calculation(price, tax):
    return price * (1 + tax)


# price_calculation = currency(price_calculation)
print(price_calculation(100, 0.05))

