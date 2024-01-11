import math
def radians_to_degree(radians):
    degrees = radians * (180/math.pi)
    return round(degrees,1)
print(radians_to_degree(1))
print(radians_to_degree(20))
print(radians_to_degree(50))
