#Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five

for num in range(101):
    if num % 10 != 0 and num % 10 != 5:
        print(num)