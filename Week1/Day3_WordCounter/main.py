# Day 3 - Word Counter

sentence = input("Enter a sentence: ")
words = sentence.split()

print("Number of words:", len(words))

for word in words:
    print(word, "length:", len(word))
