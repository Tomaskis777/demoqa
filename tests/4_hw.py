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


# class Math:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def math_method(self):
#         return self.a + self.b
#
#     def math_method2(self):
#         return self.a * self.b
#
#     def math_method3(self):
#         return self.a / self.b
#
#     def math_method4(self):
#         return self.a - self.b
#
#
# methods = Math(85, 139)
# methods2 = Math(113, 53)
# methods3 = Math(42, 95)
# methods4 = Math(280, 100)
#
#
# print(methods.math_method())
# print(methods2.math_method2())
# print(methods3.math_method3())
# print(methods4.math_method4())


class Button2level:
    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = ''

    def click(self):
        return f"Клик по кнопке {self.text}"


button_1 = Button2level("Text Box")
button_2 = Button2level("Checkbox")
button_3 = Button2level("Radio-button")
button_4 = Button2level("Webtables")
button_5 = Button2level("Buttons")
button_6 = Button2level("Links")
button_7 = Button2level("Broken")
button_8 = Button2level("Upload-download")
button_9 = Button2level("Dynamic-properties")

print(button_1.text)
print(button_2.text)
print(button_3.text)
print(button_4.text)
print(button_5.text)
print(button_6.text)
print(button_7.text)
print(button_8.text)
print(button_9.text)

print(button_1.click())
print(button_2.click())
print(button_3.click())
print(button_4.click())
print(button_5.click())
print(button_6.click())
print(button_7.click())
print(button_8.click())
print(button_9.click())
