from fastapi import FastAPI

app = FastAPI()

def some_function():
    return "What do you want?"

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

