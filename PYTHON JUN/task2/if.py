# num = 3
#
# if num > 0:
#     print('Число положительное')
#
#
# if isinstance(num, int):
#     print('Число целое')
#
# if num != 3:
#     print('число не равно 3')
#
# else:
#     print('число равно 3')
#
# my_list = []
#
# if my_list:
#     print('в списке есть значения')
# else:
#     print('в списке нет значений')
#
# if num > 0:
#     print('Число положительное')
# elif num == 0:
#     print('Число == 0')
# else:
#     print('Число отрицательное')
#
# permit = True
# my_int = 5.5
#
# if permit and my_int > 0:
#     print('Число положительное')
#
# permit = False
# if not permit and my_int > 0:
#     print('Число отрицательное')
#
# my_list = [1, 2, 3, 4]
# if 1 in my_list:
#     print('1 есть в списке')

str_1 = 'test'
str_2 = 'test1'


def task_2():
    if str_1 in str_2:
        print('ДА')
    else:
        print('НЕТ')


task_2()