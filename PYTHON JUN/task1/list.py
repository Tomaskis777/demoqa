my_list = [1, 2, 3, 4, 5]

my_list2 = [[1, 2, 3], 'text', 5.5]


print('Длина списка my_list - ', len(my_list))
print('Обращение к элементу', my_list[2])

print(my_list)
my_list[0] = 6
print(my_list)

my_list.append(7)
print(my_list)

my_list.remove(7)
print(my_list)

my_list.pop(0)
print(my_list)


