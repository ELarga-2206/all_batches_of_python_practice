# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

numbers = []

print("type 'd' to display number with most duplicate")

while True:
    user_input = input("Enter a number: ")

    if user_input == 'd':
        break

    try:
        num = int(user_input)  
        numbers.append(num)
    except ValueError:
        print("Invalid, enter a valid number.")

if numbers:
    most_duplicate_number = max(numbers, key=numbers.count)
    max_count = numbers.count(most_duplicate_number)

    if max_count > 1:
        print(f"number with most duplicates: {most_duplicate_number}")
else:
    print("No duplicates")