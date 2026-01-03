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

address_dict = {'city':'gurugram','state':'haryana','pin':'120001'}
address1 = Address(**address_dict)

patient_dict = {'name':'chinu','gender':'male','age':20,'adress':address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)

#better organizationn
#resuabaility
#redeablity
#validation