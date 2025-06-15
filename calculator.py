def add(a,b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
def modulus(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a % b

num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /, %): ")
if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)   
elif operation == '/':
    result = divide(num1, num2)
elif operation == '%':
    result = modulus(num1, num2)
else:
    result = "Invalid operation"
print("Result:", result)


'''
Enter first number: 6
Enter second number: 8
Enter operation (+, -, *, /, %): +
Result: 14.0

Enter first number: 3
Enter second number: 6
Enter operation (+, -, *, /, %,o or 'exit' ): -
Result: -3.0

Enter first number: 8
Enter second number: 9
Enter operation (+, -, *, /, %): *
Result: 72.0

Enter first number: 9
Enter second number: 3
Enter operation (+, -, *, /, %): /
Result: 3.0

Enter first number: 9
Enter second number: 0
Enter operation (+, -, *, /, %): /
Result: Error: Division by zero

Enter first number: 6
Enter second number: 16
Enter operation (+, -, *, /, %): %
Result: 6.0


'''