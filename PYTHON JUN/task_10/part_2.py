import random

x = [random.randint(-10, 10) for i in range(20)]

print(x)

with open('data.txt', 'w+') as f:

    x = list(map(lambda a: str(a)+'\n', x))

    f.writelines(x)
