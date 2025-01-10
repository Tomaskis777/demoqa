# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(-10, 10.1, 0.01)
#
#
# plt.plot(x, np.sin(x), x, np.cos(x), x, -x)
# plt.xlabel(r'$x$')
# plt.ylabel(r'$f(x)$')
# plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x$')
# plt.grid(True)
# plt.show()


# import logging
#
# try:
#     print('step 1')
#     raise Exception()
# except Exception as e:
#     logging.log(0, e)
#     print('step 2')
# finally:
#     print('step 3')


# squares = [x**2 for x in range(1, 6)]
# print(squares)  # Вывод: [1, 4, 9, 16, 25]
#
# even_squares = [x for x in squares if x % 2 == 0]
# print(even_squares) # Вывод: [4, 16, 25]

# x = 2
# print([ x for x in range(10) ])


# def is_even(n):
#     return n % 2 == 0
#
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = list(filter(is_even, numbers))
# print(result)


tlp = (a, b, c, d)
print(max(tlp))