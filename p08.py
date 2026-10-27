import statistics
try:
    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
    if len(numbers) == 0:
        raise ValueError("No numbers entered.")
    variance = statistics.pvariance(numbers)
    print("Population variance of the entered numbers is:", variance)
except ValueError:
    print("Invalid input or empty list.")