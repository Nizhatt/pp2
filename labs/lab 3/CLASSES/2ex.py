class Shape:
    def area(self):
        area = 0
        print("Area of the shape:" , area)

class Square(Shape):
    def __init__ (self,length):
        self.length = length

    def area(self):
        area = self.length*self.length
        print("Area of the square: ", area)

ex = Square(5)
ex.area()

ex1 = Shape()
ex1.area()