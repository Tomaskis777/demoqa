class Encapsulation:

    def __init__(self):
        self.open_param = {'db_name': 'student', 'db_port': '3007'}
        self.__config = {'db_user': 'root', 'db_pass': 'nnk$#Cj_Yiu'}


obj = Encapsulation()

print(obj.open_param)
# print(obj.__config)

print(obj._Encapsulation__config)
