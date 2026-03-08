from fastapi import FastAPI,Path,HTTPException,Query
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
    
@app.get("/patient/{patient_id}")
def load_patient(patient_id : str=Path(...,description="pls enter the patient id ",example="P001")):
    data=load()
    if patient_id in data:
        return data[patient_id]
    # return {"error":"patient not found"}
    raise HTTPException(status_code=404,detail="patient not found")

@app.get("/sort")
def sort_pts(sort_by : str=Query(...,description="sort on the basis of weigth,height,age"),order_by : str=Query("asc",description="sort on the basis of asc and dsc")):
    val_params=["weight","height","age"]
    if sort_by not in val_params:
        raise HTTPException(status_code=404, detail=f"pls select the valid param from {val_params}")
    if order_by not in ["asc","dsc"]:
        raise HTTPException(status_code=404,detail="pls select asc or dsc")
    
    data=load()
    sort_order=True if order_by=="asc" else False
    sorted_data= sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    return sorted_data