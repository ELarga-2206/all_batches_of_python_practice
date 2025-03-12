# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

numbers = []

print("Enter numbers: ")
print("type 's' to sort numbers")

while True:
    user_input = (input("Enter a number: "))
    if user_input == "s":
        break

    try:
        num = int(user_input)
        numbers.append(num)

    except ValueError:
        print("Invalid input! Please enter a valid number.")

numbers.sort()
for number in numbers:
    print(number)