from fastapi import FastAPI

app = FastAPI()


@app.get("/missingText")
def check_missing_text(Text: str):
    return {"Text": Text}

# 422 error means: The server received and understood the request, but it cannot process it because some required data is missing or invalid.
