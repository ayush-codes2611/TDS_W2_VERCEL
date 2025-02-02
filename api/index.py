import json
import urllib.parse
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Load student data from the JSON file
def load_data():
    with open('q-vercel-python.json', 'r') as file:
        data = json.load(file)
    return data

@app.get("/")
def get_student(name: Optional[str] = None):
    data = load_data()

    result = {"marks": []}
    if name:
        for entry in data:
            if entry["name"] == name:
                result["marks"].append(entry["marks"])

    return result

