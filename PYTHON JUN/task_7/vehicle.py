# class Vehicle:
#     def __init__(self, make, model, year, price):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.price = price
#
#     def print_info(self):
#         print(f'Марка: {self.make}'
#         f'\nМодель: {self.model}'
#         f'\nГод выпуска: {self.year}'
#         f'\nСтоимость: {self.price} руб')
#
#
# class Car(Vehicle):
#     def __init__(self, make, model, year, price, num_doors, body_style):
#         super().__init__(make, model, year, price)
#         self.num_doors = num_doors
#         self.body_style = body_style
#
#
# car = Car('Toyota', 'Camry', 2023, 50000, 5, 'Седан')
#
# car.print_info()
#
#


class A:
    def method_a(self):
        print('class a')


class B:
    def __init__(self):
        self.obj_a = A()


obj_b = B()
obj_a = A
print(obj_b.obj_a.method_a())
