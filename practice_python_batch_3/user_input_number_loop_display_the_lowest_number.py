#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

numbers = []

print("type 'l' to display the lowest number")

while True:
    user_input = input("Enter a number: ")

    if user_input == 'l':
        break

    try:
        num = int(user_input)
        numbers.append(num)

    except ValueError:
        print("Invalid input, enter a valid number.")
    
if numbers:
    lowest_number = min(numbers)
    print(f"The lowest number is: {lowest_number}")
else:
    print("No valid number")