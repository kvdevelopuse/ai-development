def get_unique_numbers(inputNumbers):
    unique_numbers = []
    for number in inputNumbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers


while True:
    inputNumbers = input("Enter a list of numbers separated by commas: ")

    is_input_valid = True

    for chars in inputNumbers:
        if chars not in "0123456789,":
            is_input_valid = False
            break

    if is_input_valid:
        numbers = inputNumbers.split(",")
        uniqueNumbers = get_unique_numbers(numbers)
        print("Unique numbers:", uniqueNumbers)
    else:
        print(
            "Error: Invalid input. Please enter a valid list of numbers separated by commas")
        continue

    continue_input = input("Do you want to continue? (y/n): ")

    if (continue_input.lower() != 'y'):
        print('Program ended.')
        break
