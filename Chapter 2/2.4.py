from fastapi import FastAPI

app = FastAPI()

@app.get("/product/{id}")
async def detail_view(id: int) -> dict:
    return {"product": f"Stock number {id}"}

@app.get("/users/{name}/{age}")
async def users(name: str, age: int) -> dict:
    return {"user_name": f"{name}", "user_age": age}

country_dict = {
    'Russia': ['Moscow', 'St. Petersburg', 'Novosibirsk', 'Ekaterinburg', 'Kazan'],
    'USA': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia'],
    'Germany': ['Berlin', 'Hamburg', 'Munich', 'Cologne', 'Frankfurt'],
    'China': ['Chunzin', 'Shanghai', 'Beijing', 'Chenddu', 'Badodin'],
    'Japan': ['Tokyo', 'Yokogama', 'Osaka', 'Nagoya', 'Sapporo'],
}

@app.get("/country/{country}")
async def list_cities(country: str, limit: int) -> dict:
    return {"country": country, "cities": country_dict[country][:limit]}