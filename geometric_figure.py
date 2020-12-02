## Unit B
#  task 6.10.1
#
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def get_settings(self):
        return Rectangle.__name__ + str ((self.x, self.y, self.width, self.height))

figure = Rectangle(5, 10, 50, 100)
print(figure.get_settings())