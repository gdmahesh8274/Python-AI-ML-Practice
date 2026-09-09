# Day 2 - Sum and Average

def calculate_sum(numbers):
    return sum(numbers)


def calculate_average(numbers):
    return calculate_sum(numbers) / len(numbers)


numbers = [10, 20, 30, 40, 50]

print("Sum:", calculate_sum(numbers))
print("Average:", calculate_average(numbers))
