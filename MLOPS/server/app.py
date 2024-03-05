from fastapi import FastAPI
from pymongo import MongoClient
app = FastAPI()


client = MongoClient('mongo', 27017)
db = client.test_database
collection = db.test_collection

def add_list_fruits(fruit):
    id = collection.insert_one({"fruit": fruit}).inserted_id
    return list(collection.find({}, {"_id": False}))

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/add/{fruit}")
async def add_fruit(fruit: str):
    id = collection.insert_one({"fruit": fruit}).inserted_id 
    return {"id": str(id)}

@app.get("/list")
async def list_fruits():
    return {"results": list(collection.find({}, {"_id": False}))}

# app/server/main.py

from pydantic import BaseModel
import joblib

app = FastAPI()

# Load the pretrained model
model = joblib.load("model.pkl")

# Define input model for FastAPI
class Item(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class_name_map= {0:"setosa",1:"versicolor",2:"virginica"}
# Prediction endpoint
@app.post("/predict")
def predict(item: Item):
    features = [[
        item.sepal_length,
        item.sepal_width,
        item.petal_length,
        item.petal_width
    ]]
    prediction = model.predict(features)[0]
    predicted=class_name_map.get(prediction,"unknown")
    return {"prediction": predicted}
