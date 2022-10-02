from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello_api():
    return {"message":"Hello punit"}