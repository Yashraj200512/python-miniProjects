from fastapi import FastAPI

# 1. Create the app object
app = FastAPI()

# 2. Create a "Route" (URL)
@app.get("/")
async def root():
    # 3. Return data
    return {"message": "Hello World", "status": "active"}

# 4. Another route that accepts data in the URL
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}