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


class Student(User):
    pass


admin_1 = Admin('Федор', '1236771865')
teacher_1 = Teacher('Федор', '1236771865')

for user in (admin_1, teacher_1):
    user.login()

print(admin_1.password)
print(admin_1.name)
print(teacher_1.name)
print(teacher_1.password)
