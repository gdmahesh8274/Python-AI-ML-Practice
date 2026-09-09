# Day 3 - Character Frequency

text = input("Enter a string: ")
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for char, count in frequency.items():
    print(char, ":", count)
