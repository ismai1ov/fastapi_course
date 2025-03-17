from fastapi import FastAPI

app = FastAPI()

@app.get('/greet')
async def greeting():
    return {"message": "Hello World"} 