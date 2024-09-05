class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        return print("Автомобиль заведён")

    def stop(self):
        return print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year

    def set_type(self, type):
        self.type = type

    def set_color(self, color):
        self.color = color


my_car = Car("красный", "седан", 2023)

# # запуск автомобиля
# my_car.start()
#
# # отключение автомобиля
# my_car.stop()
#
# # присвоение автомобилю года выпуска
# my_car.set_year(2024)
#
# # присвоение автомобилю типа
# my_car.set_type("хэтчбек")
#
# # присвоение автомобилю цвета
# my_car.set_color("синий")

print(my_car.start())
print(my_car.stop())
print(my_car.year)
print(my_car.type)
print(my_car.color)
