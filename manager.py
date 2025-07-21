from interactor import Interactor
from training import Training
from prediction import Checker
from sklearn.model_selection import train_test_split
import pandas as pd

class Manager:
    def __init__(self):
        self.interact = None
        self.df = None
        self.df_30 = None
        self.df_70 = None
        self.Trained_70_dict = {}
        self.Trained_dict = {}
        self.predict_df = None

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


