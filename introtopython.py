# Get user inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the calculation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    result = num1 / num2
else:
    print("Invalid operation. Please use +, -, *, or /.")
    exit()

# Display the result using :g to remove trailing .0 for integers
print(f"{num1:g} {operation} {num2:g} = {result:g}")