from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field,computed_field
from typing import Literal,Annotated
import pickle
import pandas as pd

#import the ml model
with open('model.pkl','rb') as f:
    model = pickle.load(f)

app = FastAPI()
tier1_cities = ["Bengaluru","Kolkata","Delhi","Mumbai","Hyderabad"]
tier2_cities = ["Jaipur","Lucknow","Pune","Patna","Chennai"]

#pydantic to validate improving data

class UserInput(BaseModel):
    age:Annotated[int,Field(...,gt=0,lt=120,description='Age of the user')]
    weight: Annotated[float,Field(...,gt=0,description='Weight of the user')]
    height: Annotated[float,Field(...,gt=0,lt=250,description='height of the user')]
    income_lpa:Annotated[float,Field(...,gt=0,description='Annual salary of the user')]
    smoker:Annotated[bool,Field(...,description='Is user smoker?')]
    city:Annotated[str,Field(...,description='City that user belongs to')]
    occupation:Annotated[Literal['sales_executive', 'software_engineer', 'business_owner','data_analyst', 'designer', 'teacher', 'farmer', 'driver',
       'product_manager', 'bank_employee', 'factory_worker',
       'government_employee', 'construction_worker', 'consultant',
       'manager'],Field(...,description='Occupation of the user')]
    
    @computed_field
    @property
    def bmi(self)->float:
        return self.weight/((self.height/100)**2)
    
    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi >30:
            return "high"
        elif self.smoker and self.bmi>27:
            return "medium"
        else :
            return "low"

    @computed_field
    @property
    def age_group(self)->str:
        if self.age<25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_age"
        return "senior"
    
    @computed_field
    @property
    def city_tier(self)->int:
        if self.city in tier1_cities:
            return 1
        else:
            return 2
    
@app.post('/predict')
def predict_premium(data: UserInput):
    input_df = pd.DataFrame([{
        'bmi':data.bmi,
        'age_group':data.age_group,
        'lifestyle_risk':data.lifestyle_risk,
        'city_tier':data.city_tier,
        'income_lpa':data.income_lpa,
        'occupation':data.occupation

    }])
    prediction = model.predict(input_df)[0]
    return JSONResponse(status_code=200,content={'predicted_category':prediction})

