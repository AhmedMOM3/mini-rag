from fastapi import FastAPI

app=FastAPI()

@app.get("/welcome")
def welcomd():
    return {
        "message":"Hello World!"
    }
