from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.post("/echoServer")
def echoServer(message: str):
    server_time = datetime.now().strftime("%H:%M:%S")

    return {
        "message": message,
        "time": server_time
    }
