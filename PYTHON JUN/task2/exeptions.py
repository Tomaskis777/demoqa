# print('123' + 123)


m = 0
# if not m:
#     raise Exception('Переменная m пустая')


try:

    if not m:
        raise Exception('Переменная m пустая')

except Exception as e:
    print(f'Зафиксировано исключение "{e}"')
