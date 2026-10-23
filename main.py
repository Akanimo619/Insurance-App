import uvicorn
from fastapi import FastAPI
from InsuranceNotes import InsuranceNote
import joblib
import numpy as np
import pandas as pd

app = FastAPI()

regressor = joblib.load('insurance_model.joblib')

MODEL_COLUMNS = [
    'Id','age','bmi','bloodpressure','children','gender_female','gender_male',
    'diabetic_No','diabetic_Yes','smoker_No','smoker_Yes', 'region_northeast',
    'region_northwest','region_southeast','region_southwest'
 ]

@app.get('/')
def index():
    return {'Hello!'}

@app.get('/name')
def get_name(name: str):
    return {'Welcome': f"{name}"}

@app.post('/predict')
def predict(data:InsuranceNote):
    df = pd.DataFrame([data.model_dump()])
    categorical_cols = ['children','gender','diabetic','smoker','region']
    encoded_df = pd.get_dummies(data=df, columns=categorical_cols)

    df_aligned = encoded_df.reindex(columns='MODEL_COLUMNS', fill_value=0)

    numeric_predictions = regressor.predict(df_aligned)

    return {
        "Prediction": float(numeric_predictions[0])
    }


if __name__== '_main_':
    uvicorn.run(app, host="127.0.0.1",port=8000)