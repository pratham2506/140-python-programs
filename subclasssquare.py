class shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class square(shape):
    def __init__(self,length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length ** 2
Shape = shape()
Square = square(float(input("Enter the side of a square : ")))
print("Area of square : ",Square.area())