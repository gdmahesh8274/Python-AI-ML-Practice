# Day 3 - Palindrome Checker

text = input("Enter a word: ")

reverse_text = ""
for char in text:
    reverse_text = char + reverse_text

if text.lower() == reverse_text.lower():
    print("Palindrome")
else:
    print("Not a palindrome")
