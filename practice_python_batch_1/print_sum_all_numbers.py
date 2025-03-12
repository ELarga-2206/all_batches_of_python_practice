#Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

total = 0 

for i in range(1, 11):
    num = int(input("enter a number:"))
    total += num

print(total)
