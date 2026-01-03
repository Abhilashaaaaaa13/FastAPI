from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pint:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address: Address

address_dict = {'city':'gurugram','state':'haryana','pin':'122001'}
address1 = Address(**address_dict)
patient_dict = {'name':'chinu','gender':'male','age':20,'adress':address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump()
print(temp)
print(type(temp))