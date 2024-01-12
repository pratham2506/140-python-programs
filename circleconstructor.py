import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        return round(math.pi * self.radius**2)
    def getPerimeter(self):
        return round(2 * math.pi * self.radius)
circy = Circle(11)
print(circy.getArea()) 
print(circy.getPerimeter())
