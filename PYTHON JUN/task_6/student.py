class Student:
    profession = 'Developer'

    def __init__(self, first_name, las_name, age):
        self.first_name = first_name
        self.last_name = las_name
        self.age = age

    def check_profession(self):
        print(self.profession)


new_student = Student('Иван', 'Петров', 22)

new_student.check_profession()
print(new_student.age)
print(new_student.first_name)
print(new_student.last_name)
