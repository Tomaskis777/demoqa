class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'{Cat.__name__}: name - {self.name}, years - {self.age}')


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def info(self):
        print(f'{Dog.__name__}: name - {self.name}, years - {self.age}, weight - {self.weight}')


cat1 = Cat('C1', 1)
dog1 = Dog('D1', 0.4, 8)

cat1.info()
dog1.info()

# for animal in (cat1, dog1):
#     animal.info()











