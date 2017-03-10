class Shape:
    def __init__(self, length):
        self.length = length

    def area(self):
        return 0


class Square(Shape):
    def __init_(self):
        super(Square, self).__init_subclass__()
    def area(self):
        return self.length**2


newSquare = Square(50)

print(newSquare.area())