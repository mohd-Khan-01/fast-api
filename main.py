from fastapi import FastAPI
import json
app=FastAPI()
def load():
    with open("patient.json","r") as f:
        data=json.load(f)
    return data



@app.get("/")
def hello():
    return {"message":"this is a patient management system"}
    
@app.get("/view")
def view():
    data=load()
    return data
    