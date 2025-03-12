#Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

#initialize empty list

#use infinite loop/while loop

numbers = []

print("Enter numbers (type 'exit' to stop):")

while True:
    user_input = input("Enter a number: ")
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break

#ask for user number input

try:
        num = int(user_input)
        if numbers.count(num) > 0:
            print(f"{num} - Duplicate")
        else:
            print(f"{num} - Unique")

            numbers.append(num)

#check if the user input is invalid:
#end


