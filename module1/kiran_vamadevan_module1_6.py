class Person:
    def __init__(self, name, contact, address, phoneNumber):
        self.name = name
        self.contact = contact
        self.address = address
        self.phoneNumber = phoneNumber

    def save_address(self):
        with open('address_book.txt', 'a') as file:
            file.write(f"Name: {self.name}\n")
            file.write(f"Contact: {self.contact}\n")
            file.write(f"Address: {self.address}\n")
            file.write(f"Phone Number: {self.phoneNumber}\n")
            file.write("\n")  # Add a newline for separation between entries


name = input("Enter your name: ")
contact = input("Enter your contact: ")
address = input("Enter your address: ")
phoneNumber = input("Enter your phone number: ")

person = Person(name, contact, address, phoneNumber)
person.save_address()

print("Address saved successfully")
