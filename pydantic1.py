from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List, Dict,Optional,Annotated
class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title='Name of the patient',description='Give the name of the patient in less than 50 chars',examples=['Chinu','Meenu'])]
    email:EmailStr
    linkedin_url: AnyUrl
    age:int
    weight:Annotated[float,Field(gt=0,strict=True)]
    married: Annotated[bool,Field(default=None,description='Is the patient married or not')]
    allergies:Annotated[Optional[List[str]],Field(default=None,max_length=5)]
    contact_details: Dict[str,str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inseted')

patient_info = {'name':'nitish','email':'abc@gmail.com','linkedin_url':'https://linkedin.com/1322','age':30,'weight':75.2,'married':True,'contact_details':{'phone':'123456789'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)