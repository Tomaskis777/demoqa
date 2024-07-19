def task_1(a=42, b=3.14, c="Hello, World!", d=[1, 2, 3], e=True):
    return a, b, c, d, e


print(task_1())


def task_2(a=(1, 2, 3, 5, 8, 13, 21)):
    return a[1], a[2], a[3]


print(task_2())


def task_3(num: int):
    return num ** 2


print(task_3(4))
