#Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))

def between(a, b):
    if a + 1 >= b:
        return
    print(a + 1)
    between(a + 1, b)

between(min(num1, num2), max(num1, num2))