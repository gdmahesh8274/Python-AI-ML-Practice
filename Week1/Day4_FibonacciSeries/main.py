# Day 4 - Fibonacci Series
# Generate the Fibonacci series for N terms using a loop.

terms = int(input("Enter number of terms: "))

first = 0
second = 1

if terms <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci Series:")

    for i in range(terms):
        print(first, end=" ")

        # The next number is the sum of the previous two numbers.
        next_number = first + second
        first = second
        second = next_number
