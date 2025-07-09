import pandas as pd

class Coach:
    def __init__(self, df):
        self.df = df
        self.coached_dict = self.coach()

    def coach(self):
        answer_col = self.df.columns[-1]
        group_cols = self.df.columns[:-1]
        total = self.df[answer_col].value_counts()
        result = {'classified': self.df[answer_col].value_counts(normalize=True).to_dict()}

        for col in group_cols:
            grouped = self.df.groupby([col, answer_col]).size().unstack(fill_value=0)
            ratio = grouped.div(total, axis=1)
            result[col] = ratio.round(3).to_dict(orient='index')

        return result