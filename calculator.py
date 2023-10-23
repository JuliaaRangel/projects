# This calculator is capable of adding, subtracting, multiplying, and dividing two numbers

# This code immediately converts integers into floats so that there aren't any errors during computation

# If user enters an invalid operator, they are notified and prompted to enter one of the valid options



num1 = float(input("Enter first number :"))
operator = input("Enter operator :")
num2 = float(input("Enter second number :"))

if operator == "+":
  print(num1 + num2)

elif operator == "-":
  print(num1 - num2)

elif operator == "*":
  print(num1 * num2)

elif operator == "/":
  print(num1 / num2)

else:
  print("Invalid operator, please enter one of the following: "+", "-", "*", "/"")

