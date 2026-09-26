from fastapi import FastAPI

app = FastAPI()


@app.get("/helloMessage")
def helloMessage(name: str):
    return {"message": "Hello " + name}
