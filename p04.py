try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = a / b
    print("Result =", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Invalid input. Please enter valid numbers.")