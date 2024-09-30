# def task_2():
#     # task_list = []
#     #
#     # for i in range(10):
#     #     task_list.append(i ** 2)
#     #
#     # print(task_list)
#     my_list = [x ** 2 for x in range(10)]
#     print(my_list)
#
#
# task_2()


# fruit_list = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
# print([x for x in fruit_list if 'a' in x])

str_list = ['continuous', 2, 'integration', 34, 'continuous', [123, 1234], 'delivery']

print(''.join([x[0].upper() for x in str_list if isinstance(x, str)]))
