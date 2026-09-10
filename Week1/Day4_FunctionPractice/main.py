# Day 4 - Functions Practice
# Functions for square, cube, factorial, and simple interest.


def square(number):
    return number * number


def cube(number):
    return number * number * number


def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result = result * i
    return result


def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


print("Square:", square(5))
print("Cube:", cube(3))
print("Factorial:", factorial(5))
print("Simple Interest:", simple_interest(1000, 5, 2))
