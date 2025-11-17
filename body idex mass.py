print("HELLO USER")

weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))
#CALCULATING BMI USING WEIGHT AND HEIGHT
BMI = weight / (height ** 2)
BMI = round(BMI, 1)

print (f"the body mass index is: {BMI}")
print("BMI Categories")

print("<18.5: underweight")
print("18.5 - 24.9: normal")
print("25 - 29.9: overweight")
print(">=30: obese")