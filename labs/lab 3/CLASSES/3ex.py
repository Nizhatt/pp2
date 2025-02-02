class Shape:
    def __init__(self, length=0):
        self.length = length

    def area(self):
        print("Area of Shape:", 0)

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

    def area(self):
        print("Area of Square:", self.length * self.length)

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width

    def area(self):
        print("Area of Rectangle:", self.length * self.width)


shape = Shape()
shape.area()  

square = Square(4)
square.area()  

rec = Rectangle(4, 5)
rec.area()  