# Encryption Rule:
# This encryption method shifts 3 postions forward in the alphabet
# For example: a --> d , b --> e, c --> f
# The last 3 letters are shifted as follows : x --> a , y --> b , z --> c
# Uppercase letters will also be shifted in the same way

def encrypt_string(input_string):
    encrypted_string = ""

    for letter in input_string:
        if letter.isalpha():
            if letter.islower():
                encrypted_string += chr((ord(letter) - 97 + 3) % 26 + 97)
            else:
                encrypted_string += chr((ord(letter) - 65 + 3) % 26 + 65)
        else:
            encrypted_string += letter

    return encrypted_string


while True:
    inputString = input("Enter a string: ")

    if (inputString == ""):
        print("Error: Please enter a valid string")
        continue
    else:
        print(encrypt_string(inputString))

    continue_input = input("Do you want to continue? (y/n): ")

    if (continue_input.lower() != 'y'):
        print('Program ended.')
        break
