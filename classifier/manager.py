import json
from pathlib import Path

class ClassificationManager:
    def __init__(self):
        self.file_path = "trained_models"

    def write_new_model_to_json(self,new_model, file_name):
        with open(f"{self.file_path}/{file_name}.json", "w") as file:
            json.dump(new_model, file)

    def check_if_model_exists(self,file_name):
        if Path(f"{self.file_path}/{file_name}.json").exists():
            return True
        else:
            return False

    def select_model(self,file_name):
        with open(f"{self.file_path}/{file_name}.json", "r") as file:
            return json.load(file)