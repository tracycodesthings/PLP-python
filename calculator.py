num1 =float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2   
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Error! Invalid operation."
print("Result:", result)
# calculator.py
# This is a simple calculator program that performs basic arithmetic operations.
# It takes two numbers and an operation as input from the user and outputs the result.
# The operations supported are addition, subtraction, multiplication, and division.
# The program also handles division by zero and invalid operations gracefully.
# Usage: Run the script and follow the prompts to enter numbers and an operation.
# The result is printed at the end.
