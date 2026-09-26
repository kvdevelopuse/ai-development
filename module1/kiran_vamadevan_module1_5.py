
def speaking_is_expensive(word, price_per_letter):
    # initialize output word
    shifted_string = ""

    # loop thru each letter in the word and shift it by 1
    for letter in word:
        if (letter == 'z'):
            shifted_string += 'a'
        elif (letter == 'Z'):
            shifted_string += 'A'
        elif letter.isalpha():
            shifted_string += chr(ord(letter) + 1)
        else:
            shifted_string += letter

    # get word count in the shifted string
    word_count = len(word.split())

    # get total letters in the shifted string
    total_letters = len(shifted_string.replace(" ", ""))

    # get price of the shifted string
    price_of_string = total_letters * price_per_letter

    return {
        "Shifted String": shifted_string,
        "Word Count": word_count,
        "Price Of String": price_of_string
    }


# print(speaking_is_expensive("speaking is expensive", 5))

sentence = input("Enter a sentence: ")
price_per_letter = input("Enter price per letter: ")

if (sentence == "" or price_per_letter == "" or price_per_letter.isdigit() == False or int(price_per_letter) < 0):
    print("Error: Invalid input. Please enter a valid sentence and a non-negative value for price")
else:
    price_per_letter = int(price_per_letter)
    print(speaking_is_expensive(sentence, int(price_per_letter)))
