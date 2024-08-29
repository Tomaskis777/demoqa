# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area_rectangle(self):
#         return self.width * self.height
#
#     def perimetr_rectangle(self):
#         return 2 * (self.width + self.height)
#
#
# condition1 = Rectangle(5, 5)
# condition2 = Rectangle(3, 6)
# condition3 = Rectangle(20, 35)
#
#
# print(condition1.area_rectangle())
# print(condition1.perimetr_rectangle())
#
# print(condition2.area_rectangle())
# print(condition2.perimetr_rectangle())
#
# print(condition3.area_rectangle())
# print(condition3.perimetr_rectangle())


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def math_method(self):
        return self.a + self.b

    def math_method2(self):
        return self.a * self.b

    def math_method3(self):
        return self.a / self.b

    def math_method4(self):
        return self.a - self.b


methods = Math(85, 139)
methods2 = Math(113, 53)
methods3 = Math(42, 95)
methods4 = Math(280, 100)


print(methods.math_method())
print(methods2.math_method2())
print(methods3.math_method3())
print(methods4.math_method4())
