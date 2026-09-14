#Q1. Variables and Data Types
name = "Rocky"
age = 40
height = 1.75
is_student = False

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

print("none")

# Q2. Input / Output
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print(f"Hello {user_name}, you are {user_age} years old.")



# Q3. If-Else

if user_age < 18:
    print("Minor")
elif user_age < 60:
    print("Adult")
else:
    print("Senior citizen") 

print("none")


# Q4. Loops
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

total = 0
n = 1
while n <= 10:
    total += n
    n += 1
print("Sum 1 to 10:", total)

print("none")

# Q5. Functions
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(2, 16):
    print(num,is_prime(num))

print("none")






