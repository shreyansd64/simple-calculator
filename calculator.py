# Simple Calculator Program 
# Author: Shreyans Dundur
# Changes: Vikash Pandey, Added more operations

print("=" * 30)
print("SIMPLE CALCULATOR")
print("=" * 30)

print("\nOperations Available:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Exponentiation (**)")
print("7. Floor Division (//)")
print("=" * 30)

# GET USER INPUT
num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+,-,*,/,%,**,//): ")

# Perform calculation
if operation == '+':
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")

elif operation == '-':
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")

elif operation == '*':
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")

elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nError: Division by zero is not allowed!")

elif operation == '%':
    if num2 != 0:
        result = num1 % num2
        print(f"\nResult: {num1} % {num2} = {result}")
    else:
        print("\nError: Division by zero is not allowed!")

elif operation == '**':
    result = num1 ** num2
    print(f"\nResult: {num1} ** {num2} = {result}")

elif operation == '//':
    if num2 != 0:
        result = num1 // num2
        print(f"\nResult: {num1} // {num2} = {result}")
    else:
        print("\nError: Division by zero is not allowed!")

else:
    print("\nError: Invalid operation entered!")

print("\nThank you for using the calculator!")
