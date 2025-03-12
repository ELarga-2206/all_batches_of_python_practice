#Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

for i in range(100):
    if i % 10 != 0:
        print(i)