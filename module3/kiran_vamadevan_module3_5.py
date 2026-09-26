from fastapi import FastAPI, Request

app = FastAPI()

person = {}


@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)

    log_message = {
        "method": request.method,
        "path": request.url.path,
        "status": response.status_code
    }

    print(log_message)

    with open("my_file.log", "a", encoding="utf-8") as file:
        file.write(str(log_message) + "\n")

    return response


@app.get("/hello")
def hello(name: str):
    return {"message": "Hello " + name}


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
