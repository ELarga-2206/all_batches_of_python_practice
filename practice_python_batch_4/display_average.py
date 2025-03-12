# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

total_sum = 0
numbers = []

print("type 'a' to display average")

while True:
    user_input = input("Enter a number: ")

    if user_input == 'a':
        break

    try:
        num = float(user_input)
        numbers.append(num)
        total_sum += num

    except ValueError:
        print("Invalid input! Please enter a valid number.")

if numbers:
    average = total_sum / len(numbers)
    print({average})