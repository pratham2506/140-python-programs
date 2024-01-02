#solve quadratic equation
# The standard form of a quadratic equation is:
# where
# a, b and c are real numbers and
# 𝑎𝑥 + 𝑏𝑥 + 𝑐 = 0
# 𝑎 ≠ 0
# The solutions of this quadratic equation is given by:
# (−𝑏 ± (𝑏^2 − 4𝑎𝑐 )^1/2)/(2𝑎)

import math
#input coefficients
a=float(input("Enter coefficient a : "))
b=float(input("Enter coefficient b : "))
c=float(input("Enter coefficient c : "))
#calculate the discriminant
discriminant=b**2-4*a*c
#check if the discriminant is positive, negetive or zero
if discriminant>0:
    #two real numbers and distinct roots
    root1=(-b+math.sqrt(discriminant))/(2*a)
    root2=(-b-math.sqrt(discriminant))/(2*a)
    print(f"Root 1 : {root1}")
    print(f"Root 2 : {root2}")
elif discriminant==0:
    #one root real (repeated)
    root=-b/(2*a)
    print(f"Root : {root}")
else:
    #complex roots
    real_part=-b/(2*a)
    imajinary_part=math.sqrt(abs(discriminant))/(2*a)
    print(f"Root 1 : {real_part}+{imajinary_part}i")
    print(f"Root 2 : {real_part}-{imajinary_part}i")
    
    
