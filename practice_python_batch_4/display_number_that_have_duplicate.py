# Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
#collect numbers from user

#check for duplicates (for i in range)
#use (set) function to keep track of numbers
#how to check for duplicates?
#must create a duplicate checker

numbers = []

for i in range(1,11):
    num = int(input("enter a number: "))
    numbers.append(num)

print("No duplicates: ")
for num in numbers:
    if numbers.count(num) == 1:
        print(num)