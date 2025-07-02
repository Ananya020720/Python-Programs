num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if num1 == num2 == num3:
  print("All three given numbers are equal")
if num1 <= num2 and num1 <= num3:
  print(f"Smallest of {num1}, {num2} and {num3} is {num1}")
elif num2 <= num1 and num2 <= num3:
  print(f"Smallest of {num1}, {num2} and {num3} is {num2}")
else:
  print(f"Smallest of {num1}, {num2} and {num3} is {num2}")
