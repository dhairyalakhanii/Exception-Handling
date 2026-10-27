try:
    n=int(input("Enter a number of values: "))
    if n<=0:
        raise ValueError("N must be positive.")
    numbers=[]
    for i in range(n):
        num=float(input(f"Enter a number: "))
        numbers.append(num)
    mean=sum(numbers)/n
    print(f"The mean of the entered numbers is: {mean}")
except ValueError:
    print("Invalid input. Enter a valid number.")