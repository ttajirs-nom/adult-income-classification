from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

app = FastAPI()

class UserInput(BaseModel):
    age: int
    workclass: str
    fnlwgt: int
    education: str
    educational_num: int
    marital_status: str
    occupation: str
    relationship: str
    race: str
    gender: str
    capital_gain: int
    capital_loss: int
    hours_per_week: int
    native_country: str


@app.get("/")
def home():
    return {"message": "Adult Income Prediction API Running"}


@app.post("/predict")
def predict(data: UserInput):

    input_dict = data.dict()

    input_df = pd.DataFrame([input_dict])

    input_df = input_df.rename(columns={
        "marital_status": "marital-status",
        "hours_per_week": "hours-per-week",
        "educational_num": "educational-num",
        "capital_gain": "capital-gain",
        "capital_loss": "capital-loss",
        "native_country": "native-country"
    })

    prediction = model.predict(input_df)

    return {
        "prediction": prediction[0]
    }
