from fastapi import FastAPI, status, Body
from pydantic import BaseModel

class Message(BaseModel):
    id: int
    text: str

app = FastAPI()

messages_db = []


# getting all data
@app.get("/")
async def get_all_messages() -> dict:
    return {"Messages": messages_db}


# getting data by identifier
@app.get("/message/{message_id}")
async def get_message(message_id: int):
    return messages_db[message_id]


# adding data
@app.post("/message", status_code=status.HTTP_201_CREATED)
async def create_message(message:Message) -> str:
    if messages_db:
        message.id = max(messages_db, key=lambda m: m.id).id + 1
    else:
        message.id = 0
    messages_db.append(message)
    return "Message created!"


# change data
@app.put("/message/{message_id}")
async def update_message(message_id:int, message:str = Body()) -> str:
    messages_db[message_id] = message
    return "Message updated!"


# deleting data by identifier
@app.delete("/message/{message_id}")
async def delete_message(message_id: int) -> str:
    messages_db.pop(message_id)
    return f"Message ID = {message_id} deleted!"


# deleting all data
@app.delete("/")
async def kill_message_all() -> str:
    messages_db.clear()
    return "All messages deleted!"