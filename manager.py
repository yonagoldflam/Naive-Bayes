import json
from interactor.interactor import Interactor
from training.training import Training
from classifier.classifier import Classifier


class Manager:
    def __init__(self):
        self.interact = Interactor()
        self.df = None
        self.trained_dict = {}

    def update_model(self,data_url):
        self.interact.get_data(data_url)
        self.df = self.interact.df
        t = Training(self.df,self.interact.file_name)
        self.trained_dict = t.trained_dict
        return 'good'

    def select_data(self,data_name):
        with open(f"model_files/{data_name}.json", 'r') as file:
            self.trained_dict = json.load(file)


    def predict(self, row_dict):
        classifier = Classifier(self.trained_dict)
        classifier_response = classifier.classifier(row_dict)
        return classifier_response


