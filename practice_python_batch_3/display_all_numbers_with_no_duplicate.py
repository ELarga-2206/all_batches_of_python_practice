#Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

numbers = []

for i in range(1,11):
    num = int(input("enter a number: "))
    numbers.append(num)

print("No duplicates: ")
for num in numbers:
    if numbers.count(num) == 1:
        print(num)
