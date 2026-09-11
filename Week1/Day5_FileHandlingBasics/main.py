# Day 5 - File Handling Basics
# Practice writing, appending, and reading a text file.

file_name = "practice.txt"

# Write to the file safely.
with open(file_name, "w") as file:
    file.write("Python file handling practice.\n")

# Append more text to the file.
with open(file_name, "a") as file:
    file.write("This line was appended to the file.\n")

# Read and display the file contents.
with open(file_name, "r") as file:
    content = file.read()

print(content)
