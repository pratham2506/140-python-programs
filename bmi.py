def bodymass(height,weight):
    return round((weight/height**2),2)
h = float(input("Enter your height in meters : "))
w = float(input("Enter your weight is kgs : "))
print("Welcome to the BMI calculator")
bmi = bodymass(h,w)
print("Your BMI is : ",bmi)
if bmi <= 18.5:
    print("You are underweight")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal")
else: 
    print("You are obese")