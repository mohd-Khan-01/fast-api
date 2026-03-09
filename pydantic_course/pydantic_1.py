from pydantic import BaseModel,AnyUrl,Field
from typing import Optional,List,Dict,Annotated

class Patient(BaseModel):
    age : Annotated[int,Field(default=None,examples="21,31,12",description="pls enter the age of patient")]
    name :str=Field(max_length=50)
    allergies:Optional[List[str]]=None
    contact:Dict[str,str]
    
def update_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.contact)

patient_info={"name":"vikah","age":27,"allergies":["pollene","sun"],"contact":{"email":"xyz@gmail","phone":"0202011"}}
patient_1=Patient(**patient_info)

update_patient(patient_1)
