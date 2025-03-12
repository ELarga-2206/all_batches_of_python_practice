# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

numbers = []

print("type 'h' to display the lowest number")

while True:
    user_input = input("Enter a number: ")

    if user_input == 'h':
        break

    try:
        num = int(user_input)
        numbers.append(num)

    except ValueError:
        print("Invalid input, enter a valid number.")
    
if numbers:
    highest_number = max(numbers)
    print(f"The lowest number is: {highest_number}")
else:
    print("No valid number")