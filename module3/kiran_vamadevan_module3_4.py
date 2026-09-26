from fastapi import FastAPI

app = FastAPI()

person = {}


@app.post("/saveDetails")
def save_details(name: str, phone_number: int):
    person["name"] = name
    person["phone_number"] = phone_number

    return person


@app.get("/getDetails")
def get_details():
    name_number = 0

    for character in person["name"]:
        name_number = name_number + ord(character)

    random_number = name_number % 10

    return {
        "name": person["name"],
        "phone_number": person["phone_number"],
        "random_number": random_number
    }
