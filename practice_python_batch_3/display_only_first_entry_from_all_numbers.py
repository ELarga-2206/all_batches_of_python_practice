# Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

numbers = []

for i in range(1,11):
    num = int(input("enter a number: "))
    numbers.append(num)

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("numbers with no duplicates:")
for num in unique:
    print(num)
