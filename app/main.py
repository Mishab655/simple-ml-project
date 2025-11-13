from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict

app = FastAPI()

class InputData(BaseModel):
    instances: list

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.post('/predict')
def get_prediction(data: InputData):
    results = predict(data.instances)
    return {'predictions': results}
