print("Welcome to the BMI calculator")
weight = int(input("Enter your wieght = "))
height = float(input("Enter your height = "))
BMI = weight / height ** 2
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you are overweight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obesse")
else:
    print(f"Your BMI is {BMI}, you are clincly obeese")
