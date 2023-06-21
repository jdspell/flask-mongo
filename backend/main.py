from pymongo import MongoClient
from fastapi import FastAPI

app = FastAPI()

client = MongoClient('mongodb://localhost:27017/')
db = client.database_name

@app.get("/")
async def root():
    # get a collection
    collection = db.collection_name

    # insert a document
    doc = {"name": "John", "age": 30, "city": "New York"}
    collection.insert_one(doc)

    # query a document
    query = {"name": "John"}
    doc = collection.find_one(query)
    print(doc)
    return {"message": "hello"}