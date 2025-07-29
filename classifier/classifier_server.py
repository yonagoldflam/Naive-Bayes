import uvicorn as uv
from fastapi import FastAPI
import requests
from prediction import Classifier
cla = Classifier()
app = FastAPI()


def get_trained_model(base_url):
    response = requests.get(f"{base_url}/trained")
    print(response.status_code)
    return response.json()

app = FastAPI()

@app.post("/classify")
def classify(vector: dict[str, str]):
    trained_model = get_trained_model('http://model:9000')
    print(trained_model)
    return {'resalt':(cla.classifier(trained_model,vector))}
