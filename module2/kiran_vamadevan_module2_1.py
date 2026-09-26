def check_number_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


while True:
    inputNumber = input("Enter a number: ")

    if inputNumber.strip() == "" or inputNumber == "" or not inputNumber.isdigit() or int(inputNumber) < 0:
        print("Error: Please enter a valid number")
        continue
    else:
        print(check_number_even_or_odd(int(inputNumber)))

    continue_input = input("Do you want to continue? (y/n): ")

    if (continue_input.lower() != 'y'):
        print('Program ended.')
        break
