import json
class Training:
    def __init__(self, df,file_name='validate'):
        self.df = df
        self.trained_dict = self.training()
        self.write_to_json_file(file_name)

    def training(self):
        answer_col = self.df.columns[-1]
        group_cols = self.df.columns[:-1]
        total = self.df[answer_col].value_counts()
        result = {'classified': self.df[answer_col].value_counts(normalize=True).to_dict()}

        for col in group_cols:
            grouped = self.df.groupby([col, answer_col]).size().unstack(fill_value=0)
            ratio = grouped.div(total, axis=1)
            result[col] = ratio.round(3).to_dict(orient='index')

        return result

    def write_to_json_file(self,file_name):
        with open(f"data/{file_name}.json", "w") as file:
            json.dump(self.trained_dict, file)

