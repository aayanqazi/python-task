class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width


newRectangle = Rectangle(50, 50)

print(newRectangle.area())