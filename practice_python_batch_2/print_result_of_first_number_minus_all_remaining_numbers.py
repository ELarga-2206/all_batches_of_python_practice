#Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

counter = 0 

for _ in range (10):
    num = int(input("Enter a number:"))
    counter -= num
        
print(counter)