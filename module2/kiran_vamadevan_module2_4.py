import json


class Person:
    def __init__(self, name, number, location, job_title):
        self.name = name
        self.number = number
        self.location = location
        self.job_title = job_title

    def get_person_details(self):
        return {
            "name": self.name,
            "number": self.number,
            "location": self.location,
            "job_title": self.job_title
        }


person1 = Person("Kiran", 648, "Abu Dhabi", "Engineer")
person2 = Person("Manju", 748, "Abu Dhabi", "Technician")
person3 = Person("Meghna", 848, "Sharjah", "Supervisor")
person4 = Person("Mehul", 548, "Dubai", "Program Manager")
person5 = Person("Rohit", 448, "Dubai", "Pilot")


people = [
    person1.get_person_details(),
    person2.get_person_details(),
    person3.get_person_details(),
    person4.get_person_details(),
    person5.get_person_details()
]


with open("people.json", "w") as file:
    json.dump(people, file, indent=4)


print("People details saved successfully.")
