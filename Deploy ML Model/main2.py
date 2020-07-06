from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib
import pandas as pd
from process_input_data import get_prepared_data

templates = Jinja2Templates(directory='templates')

app = FastAPI()

class HousePredictionPayload(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: int
    total_rooms: int
    total_bedrooms: int
    population: int
    households: int
    median_income: float
    ocean_proximity: str

# Load my test data
test_vectorized = open('model/X_test_vectorized.pkl', 'rb')
test_cv = joblib.load(test_vectorized)

# Load our model
housing_model = open('model/final_model_aems_housing.pkl', 'rb')
housing_reg = joblib.load(housing_model)

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(name='index.html', context={
        'request': request
    })


# Predict test data
@app.get('/predict/')
def predict():
    prediction = housing_reg.predict(test_cv)
    resTop10 = prediction.tolist()[0:10]

    if(len(resTop10) > 0):
        return { 'predicted_values': resTop10}
    else:
        return {}

@app.get('/test_results')
def test_results_fn(request: Request):
    return templates.TemplateResponse(name='test_results.html', context={
        'request': request,
        'test_results_predictions': predict()
    })

@app.post('/predict/')
def predict_for_one(request: Request, input: HousePredictionPayload):
    # create pandas dataframe
    payload = {
        "longitude": input.longitude,
        "latitude": input.latitude,
        "housing_median_age": input.housing_median_age,
        "total_rooms": input.total_rooms,
        "total_bedrooms": input.total_bedrooms,
        "population": input.population,
        "households": input.households,
        "median_income": input.median_income,
        "ocean_proximity": input.ocean_proximity
    }
    payload = pd.DataFrame([payload])
    resp = get_prediction(payload)
    return {
        'result': resp.tolist()
    }
    # return the results
    # return templates.TemplateResponse(name='index.html')

def get_prediction(payload):
    # convert raw data to ML format (preprocess)
    data_prepared = get_prepared_data(payload)

    # predict on preprocess data
    prediction_data = housing_reg.predict(data_prepared)
    return prediction_data
