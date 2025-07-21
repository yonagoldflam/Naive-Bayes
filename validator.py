import json
from prediction import Checker
from training import Training
from sklearn.model_selection import train_test_split
import pandas as pd

class Validator:
    def __init__(self):
        self.df = None
        self.df_30 = None
        self.df_70 = None
        self.trained_70_dict = {}
        self.validate_resalt = None

    def validate_model(self, df):
        self.df = df
        self.cat_df()
        self.coached_df()
        self.validate_resalt = self.prediction_df()
        return self.validate_resalt

    # def read_data(self):
    #     with open('trained_data.json', 'r') as file:
    #         self.coached_dict = json.load(file)

    def cat_df(self):
        target_column = self.df.columns[-1]
        self.df_70, self.df_30 = train_test_split(
            self.df,
            test_size=0.3,
            random_state=42,
            stratify=self.df[target_column]
        )

    def coached_df(self):
        coach = Training(self.df_70)
        self.trained_70_dict = coach.Trained_dict

    def prediction_df(self):
        self.df_30 = self.df_30.iloc[:, :-1].to_dict(orient='records')
        checker = Checker(self.trained_70_dict)
        count_corect = 0
        count_uncorect = 0
        for row_dict in self.df_30:
            answer_pred = checker.prediction(row_dict)[0]

            mask = (self.df[list(row_dict)] == pd.Series(row_dict)).all(axis=1)
            if self.df.loc[mask, self.df.columns[-1]].iloc[0] == answer_pred:
                count_corect += 1
            else:
                count_uncorect += 1

        return (count_corect / (count_uncorect + count_corect)) * 100

