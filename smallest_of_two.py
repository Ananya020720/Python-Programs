num1 = int(input("Enter First Number: "))
num2 = int(input("Enter second Number: "))

if num1 < num2:
  print(f"Smallest of {num1}, {num2} is {num1}")
elif num2 < num1:
  print(f"Smallest of {num1}, {num2} is {num2}")
else:
  print("Both the given numbers are equal")
