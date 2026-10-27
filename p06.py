frequency = {"apple": 5, "banana": 3, "mango": 7}
try:
    key = input("Enter the fruit name: ")
    print("Frequency of", key, "is:", frequency[key])
except KeyError:
    print("Fruit not found in the dictionary.")