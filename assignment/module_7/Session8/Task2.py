#Use the math module to build a BMI calculator in bmi_calc.py. Take weight (kg) and height (meters) as input, use math.pow() for squaring, and print the calculated BMI rounded to 2 decimals.

import math

weight = int(input("Enter Weight = "))
height = int(input("Enter height = "))

bmi = weight / math.pow(height, 2)
print("BMI:", round(bmi, 2))