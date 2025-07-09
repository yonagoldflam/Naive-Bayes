from types import new_class

import pandas as pd

df = pd.read_csv('C:/Users/HOME/OneDrive/שולחן העבודה/data python/buy_computer_data.csv')

def answer_ratios_for_all_columns(df):
    answer_col = df.columns[-1]
    group_cols = df.columns[:-1]
    total = df[answer_col].value_counts()
    result = {}

    for col in group_cols:
        grouped = df.groupby([col, answer_col]).size().unstack(fill_value=0)
        ratio = grouped.div(total, axis=1)
        result[col] = ratio.round(3).to_dict(orient='index')

    return result

result = answer_ratios_for_all_columns(df)

def disply(values_dict,resalt_dict):
    yes = 0
    no = 0
    for k,v in values_dict.items():
        yes *= resalt_dict[k][v]['yes']
        no *= resalt_dict[k][v]['no']
    if yes > no:
        return f'yes  {yes}'
    else:
        return f'no   {no}'











