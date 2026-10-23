from pydantic import BaseModel

class InsuranceNote(BaseModel):
    Id: int
    age: int
    gender: object
    bmi: float
    bloodpressure: int
    diabetic: object
    children: object
    smoker: object
    region: object