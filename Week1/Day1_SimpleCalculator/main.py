# Day 1 - Simple Calculator
# Menu-based calculator for basic arithmetic operations.

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choose an operation (1-4): ")

try:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    if choice == "1":
        result = first + second
    elif choice == "2":
        result = first - second
    elif choice == "3":
        result = first * second
    elif choice == "4":
        if second == 0:
            print("Error: Cannot divide by zero.")
            result = None
        else:
            result = first / second
    else:
        print("Invalid operation.")
        result = None

    if result is not None:
        print("Result:", result)

except ValueError:
    print("Invalid input. Please enter numbers.")
