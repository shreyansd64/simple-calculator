#Simple Calculator Program 
#Author:Shreyans dundur
#canges:Vikash pandey
print("=" * 30)
print("SIMPLE CALCULATOR")
print("=" *30)

print("\nOperations Available:")
print("1. Addition (+)")
print("2.Subtraction (-)")
print("3.Multiplication (*)")
print("4.Division (/)")
print("=" * 30)

#GET USER INPUT
num1=float(input("\nEnter first number:"))
num2=float(input("Enter second number:"))
operation=input("Enter operation (+,-,*,/):")

#perform calculation
if operation == '+':
  result = num1 + num2
  print(f"\n Result: {num1} + {num2} = {result}")

elif operation == '-':
  result = num1 - num2
  print(f"\n Result: {num1} - {num2} = {result}")

elif operation == '*':
  result = num1 * num2
  print(f"\n Result: {num1} * {num2} = {result}")

elif operation == '/':
  if num2 != 0:
    result = num1 / num2
    print(f"\n Result: {num1} / {num2} = {result}")
  else:
    print("\n Error: Invalid operation!")

print("\nThank you for using the calculator!")
