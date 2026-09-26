def display_string(string_value):
    try:
        if string_value.isdigit():
            raise TypeError("Input must be a string")
        return string_value
    except TypeError:
        return None


while True:
    inputString = input("Enter a sentence: ")

    if inputString == "":
        print("Error: Invalid input. Please enter a valid string")
        continue
    else:
        print(display_string(inputString))

    continue_input = input("Do you want to continue? (y/n): ")

    if (continue_input.lower() != 'y'):
        print('Program ended.')
        break
