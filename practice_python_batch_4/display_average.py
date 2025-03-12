# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

#average
# user inputs + user inputs / no of user inputs
# must have counter of user inputs
# must add the number to the list and update the total sum

# counter = 0
#while loop
#user input
#append valid inputs, then add their values
#once added should be divided to total of inputs (valid numbers only, no alphabet)

total_sum = 0
numbers = []

print("type 'a' to display average")

while True:
    user_input = input("Enter a number: ")

    if user_input == 'a':
        break

    try:
        num = int(user_input)
        numbers.append(num)
        total_sum += 1

    except ValueError:
        print("Invalid input! Please enter a valid number.")

if numbers:
    average = total_sum / len(numbers)
    print({average})