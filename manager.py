from interactor import Interactor
from training import Training
from prediction import Checker


class Manager:
    def __init__(self):
        self.interact = None
        self.df = None
        self.Trained_dict = {}

    def update_model(self,data_url):
        self.interact = Interactor(data_url)
        self.df = self.interact.df
        t = Training(self.df)
        self.Trained_dict = t.Trained_dict
        return 'good'

    def predict(self, row_dict):
        checker = Checker()
        response = checker.prediction(row_dict)
        return response


