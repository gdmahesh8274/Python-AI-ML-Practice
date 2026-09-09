# Day 1 - Even/Odd Checker
# Take five numbers and determine whether each is even or odd.

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))
    print(f"{number} is {check_even_odd(number)}")
