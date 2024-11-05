import matplotlib.pyplot as plt


def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fib1 = fib2 = 1
    res = [fib1, fib2]
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        res.append(fib2)
    return res


print(fib(10))

plt.plot(fib(12))
plt.show()
