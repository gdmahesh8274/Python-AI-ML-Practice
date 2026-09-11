# Day 5 - Mini Practice Set
# Three short problems using concepts learned during Week 1.

# Problem 1: Find even numbers in a list.
numbers = [10, 15, 22, 33, 40]
print("Even numbers:")
for number in numbers:
    if number % 2 == 0:
        print(number)

# Problem 2: Count vowels in a word.
word = input("\nEnter a word: ")
vowel_count = 0
for char in word.lower():
    if char in "aeiou":
        vowel_count += 1
print("Vowel count:", vowel_count)

# Problem 3: Calculate factorial using a function.
def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


number = int(input("\nEnter a number for factorial: "))
print("Factorial:", factorial(number))
