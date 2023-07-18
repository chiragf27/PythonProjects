height = input("Enter height in cm")
weight = input("Enter weight in Kg")
int(weight)
float(height)
bmi = round(weight/height**2)
if bmi <18.5:
    print(f"Your bmi is {bmi}, you are Underweight")
elif bmi <= 25:
    print(f"Your bmi is {bmi}, you are Normal weight")
elif bmi <= 30:
    print(f"Your bmi is {bmi}, you are Overweight")
elif bmi <= 35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")