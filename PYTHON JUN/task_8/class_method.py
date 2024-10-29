from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @abstractmethod
    def login(self):
        pass


class Admin(User):
    def login(self):
        print(f'{self.name} - login')


class Teacher(User):
    def login(self):
        print(f'{self.name} - login')
        print(f'{self.password} - password')


class Student(User):
    pass


class Magistr(Student):
    def login(self):
        print(f'{self.name} - login')


admin_1 = Admin('Федор', '1236771865')
teacher_1 = Teacher('Anus', '1236771865')
student_m = Magistr('Maga', '63743673')

for user in (admin_1, teacher_1, student_m):
    user.login()

# print(admin_1.password)
# print(admin_1.name)
# print(teacher_1.name)
# print(teacher_1.password)

