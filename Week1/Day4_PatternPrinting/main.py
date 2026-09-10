# Day 4 - Pattern Printing
# Three star patterns using nested loops.

rows = 5

print("Pattern 1:")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nPattern 2:")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nPattern 3:")
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
