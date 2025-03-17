from fastapi import FastAPI, Path, Query

app = FastAPI()

#1

@app.get("/user/{name}")
async def user(name: str = Path(min_length=4,
                                max_length=20,
                                description="Enter your name")):
    return {"user_name": name}

#2

@app.get("/category/{category_id}/products")
async def category(page: int, 
                   category_id: int = Path(gt=0,
                                           description="Category ID")):
    return {"category_id": category_id, "page": page}

profiles_dict = {
    'alex': {'name': 'Александр', 'age': 33, 'phone': '+79463456789', 'email': 'alex@my-site.com'},
}

#3

@app.get("/users")
async def retrieve_user_profile(username: str = Query(min_length=2,
                                                      max_length=50,
                                                      description="Имя пользователя")):
    if username in profiles_dict:
        return profiles_dict.get(username)
    else:
        return {"message": f"Пользователь {username} не найден."}