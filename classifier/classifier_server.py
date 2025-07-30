import uvicorn as uv
from fastapi import FastAPI
import requests
from classifier import Classifier
from manager import ClassificationManager

class ClassificationServer:
    def __init__(self):
        self.app = FastAPI()
        self.manager = ClassificationManager()
        self.classifier = Classifier()
        self.model_url = "http://model-container:9000"
        self.classify()

    def update_new_model(self,api, model_name):
        current_model = self.get_trained_model(api, model_name)
        self.manager.write_new_model_to_json(current_model, model_name)
        return current_model

    def get_trained_model(self, api: str, model_name: str):
        response = requests.get(f"{self.model_url}/{api}", headers={"model-name": model_name})
        print(response.status_code)
        return response.json()

    def classify(self):
        @self.app.post("/classify")
        def classify(vector: tuple[dict[str, str],str]):
            if self.manager.check_if_model_exists(vector[1]):
                current_model = self.manager.select_model(vector[1])
            else:
                current_model = self.update_new_model(api='trained', model_name=vector[1])
            result = self.classifier.classifier(current_model, vector[0])
            return {"result": result}

server = ClassificationServer()
app = server.app
