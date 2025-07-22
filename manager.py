import json
from interactor import Interactor
from training import Training
from prediction import Checker


class Manager:
    def __init__(self):
        self.interact = Interactor()
        self.df = None
        self.Trained_dict = {}

    def update_model(self,data_url):
        self.interact.get_data(data_url)
        self.df = self.interact.df
        t = Training(self.df,self.interact.file_name)
        self.Trained_dict = t.Trained_dict
        return 'good'

    def select_data(self,data_name):
        with open(f"../model files/{data_name}.json", 'r') as file:
            self.Trained_dict = json.load(file)


    def predict(self, row_dict):
        checker = Checker(self.Trained_dict)
        response = checker.prediction(row_dict)
        return response


