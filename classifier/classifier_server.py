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
    trained_model = get_trained_model('http://main-server:8000')
    print(trained_model)
    return {'resalt':(cla.classifier(trained_model,vector))}

# @app.post("/predict")
# def predict(vector: dict[str, str]):
#     trained_model = get_trained_model('http://127.0.0.1:8080')
#     print(trained_model)
#     return {'resalt':(cla.classifier(trained_model,vector))}

# if __name__ == '__main__':
#     uv.run("classifier_server:app", host='127.0.0.1', port=8090,reload=True)

#{'classified': {'yes': 0.6428571428571429, 'no': 0.35714285714285715}, 'age': {'31...40': {'no': 0.0, 'yes': 0.444}, '<=30': {'no': 0.6, 'yes': 0.222}, '>40': {'no': 0.4, 'yes': 0.333}}, 'income': {'high': {'no': 0.4, 'yes': 0.222}, 'low': {'no': 0.2, 'yes': 0.333}, 'medium': {'no': 0.4, 'yes': 0.444}}, 'student': {'no': {'no': 0.8, 'yes': 0.333}, 'yes': {'no': 0.2, 'yes': 0.667}}, 'credit_rating': {'excellent': {'no': 0.6, 'yes': 0.333}, 'fair': {'no': 0.4, 'yes': 0.667}}}