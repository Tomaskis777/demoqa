my_list = [1, 2, 3, 4, 5, 6, 7]

for i in my_list:
    print(i ** 2)


my_str = 'строка'

for i in my_str:
    print(i)


def task_1(task_list):
    results = 0
    for x in task_list:
        results = results + x
        return results


def task_1_v2(task_list):
    return sum(task_list)


task_1_list = [1, 2, 3, 4, 5, 6, 7]
task_1(task_1_list)

print(task_1_v2(task_1_list))
print(task_1(task_1_list))
