#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

#same process
#initialize
#function
#while loop
#exit condition
#input handling
#append function
#find the lowest number input

number = []

while True:
    user_input = input("Enter a number: ")

    if user_input == 'l':
        break

 try:
    num = int(user_input)
    numbers.append(num)

    except ValueError:
        print("Invalid input! Please enter a valid number.")
    
    if numbers:
    low_num = min(numbers)
    print("The lowest number is: {low_num}")
else:
    print("No valid num")

#fix indentions bro wyd
print("type 'l' to display the lowest number")
