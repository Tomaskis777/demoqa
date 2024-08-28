class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_rectangle(self):
        return self.width * self.height


    def perimetr_rectangle(self):
        return 2 * (self.width + self.height)

condition1 = Rectangle(5, 5)
condition2 = Rectangle(3, 6)

print( condition1.area_rectangle())
print(condition2.perimetr_rectangle())


