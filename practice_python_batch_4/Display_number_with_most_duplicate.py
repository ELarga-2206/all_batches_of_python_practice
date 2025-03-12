# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

numbers = []

print("type 'd' to display number with most duplicate")

while True:
    user_input = input("Enter a number: ")

    if user_input == 'd':
    break
