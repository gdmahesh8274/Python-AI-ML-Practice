# Day 3 - String Operations


def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count


text = input("Enter a string: ")

print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Reverse:", text[::-1])
print("Vowel count:", count_vowels(text))
