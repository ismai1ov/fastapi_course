# Необходимо создать простой REST API на FastAPI для управления списком заметок (To-Do).

# API должен поддерживать обработку GET запросов, 
# а именно обрабатывать операцию получения списка всех заметок и получение информациио 
# конкретной заметке по её ID.

# GET /todos/: Получение всех заметок. Возвращает словарь заметок.
# GET /todos/{todo_id}: Получение информации о конкретной заметке по ID. Возвращает текст заметки.

from fastapi import FastAPI, Body, status

app = FastAPI()

todo_db = {0: "The first note"}


@app.get("/todos")
async def get_all_tasks() -> dict:
    return todo_db


@app.get("/todos/{todo_id}")
async def get_task(todo_id: int) -> str:
    return todo_db[todo_id]


@app.delete("/todos/delete_all")
async def delete_all():
    todo_db.clear
    return "All tasks deleted!"


@app.post("/todos/add_task", status_code=status.HTTP_201_CREATED)
async def add_task(task: str = Body()):
    current_id = int(max(todo_db, key=int)) + 1
    todo_db[current_id] = task
    return "New task created!"