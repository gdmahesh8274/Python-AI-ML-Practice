# Day 2 - Find Largest and Smallest

numbers = [12, 5, 8, 20, 3, 15]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print("Largest:", largest)
print("Smallest:", smallest)
