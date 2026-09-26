def get_address_word_count():
    with open('address_book.txt', 'r') as file:
        lines = file.readlines()

        new_lines = []
        address_word_count = 0

        for line in lines:
            if line.startswith("Address:"):
                address = line.replace("Address", "").strip()
                address_word_count = len(address.split())

            new_lines.append(line)

            if line.startswith("Phone"):
                new_lines.append("Address Word Count: " +
                                 str(address_word_count) + "\n")

    with open("address_book.txt", "w") as file:
        file.writelines(new_lines)


get_address_word_count()

print("Word count added successfully.")
