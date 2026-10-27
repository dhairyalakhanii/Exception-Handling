import statistics
try:
    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
    if len(numbers) == 0:
        raise ValueError("No numbers entered.")
    sd = statistics.pstdev(numbers)
    print(f"The standard deviation of the entered numbers is: {sd}")
except ValueError:
    print("Invalid numerical value !")