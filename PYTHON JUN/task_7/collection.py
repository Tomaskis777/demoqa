class Collection:
    def __init__(self, my_list):
        self.my_list = my_list

    def __len__(self):
        return len(self.my_list)

    def __del__(self):
        print('удаляется объект класса Collection')


obj1 = Collection([1, 2, 3, 4])


obj1.my_list
print(len(obj1))

# del obj1
#
# print(obj1)
