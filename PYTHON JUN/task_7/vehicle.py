class Person:
    def __init__(self, firs_name, last_name):
        self.first_name =firs_name
        self.last_name = last_name


class Student(Person):
    def __init__(self, course, firs_name, last_name):
        self.course = course
        super().__init__(firs_name,last_name)

