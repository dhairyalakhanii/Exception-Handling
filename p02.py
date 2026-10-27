import statistics
try:
    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
    if len(numbers) == 0:
        raise ValueError("No numbers entered.")
    median = statistics.median(numbers)
    print(f"The median of the entered numbers is: {median}")
except ValueError:
    print("Invalid input or empty list.")