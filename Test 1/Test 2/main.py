## Loops
for i in range(5):
    print(i)

## Strings
name = "Mahesh"

print(name)
print(name.upper())
print(name[0]) 

##Lists
cars = ["BMW", "Volvo", "Ford"]
print(cars)
print(cars[0])
print(len(cars))


## Functions

def print_even_numbers():
    numbers = [1, 2, 3, 4, 5]

    for num in numbers:
        if num % 2 == 0:
            print(num)

print_even_numbers() 
