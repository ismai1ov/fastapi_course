from fastapi import FastAPI, status, Body

app = FastAPI()

messages_db = {0: "First post in FastAPI"}


# getting all data
@app.get("/")
async def get_all_messages() -> dict:
    return messages_db


# getting data by identifier
@app.get("/message/{message_id}")
async def get_message(message_id: int) -> str:
    return messages_db[message_id]


# adding data
@app.post("/message", status_code=status.HTTP_201_CREATED)
async def create_message(message:str = Body()) -> str:
    current_index = int(max(messages_db, key=int)) + 1
    messages_db[current_index] = message
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