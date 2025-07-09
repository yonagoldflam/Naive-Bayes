# from multiprocessing.connection import default_family

import pandas as pd
from unicodedata import normalize


def answer_ratios_for_all_columns(df):
    answer_col = df.columns[-1]
    print(type(answer_col))
    group_cols = df.columns[:-1]
    total = df[answer_col].value_counts()
    result = {answer_col : df[answer_col].value_counts(normalize=True).to_dict()}

    for col in group_cols:
        grouped = df.groupby([col, answer_col]).size().unstack(fill_value=0)
        ratio = grouped.div(total, axis=1)
        result[col] = ratio.round(3).to_dict(orient='index')


    return result




data = {
    'category':  ['A', 'B', 'A', 'C', 'A', 'B','C'],
    'category2': ['D', 'E', 'D', 'F', 'D', 'E','F'],
    'answer':    ['yes', 'no', 'yes', 'yes', 'no', 'yes','no']
}

df = pd.DataFrame(data)
result = answer_ratios_for_all_columns(df)
print(result)




# d = {}
#
# d['apple'] = d.get('apple', 0) + 1
# d['apple'] = d.get('apple', 0) + 1
# print(d)

# def count_answers_by_column(df, group_col, answer_col):
#     grouped = df.groupby([group_col, answer_col]).size().unstack(fill_value=0)
#     return {group_col: grouped.to_dict(orient='index')}
# def answer_ratio_by_group(df, group_col, answer_col):
#     grouped = df.groupby([group_col, answer_col]).size().unstack(fill_value=0)
#     total = df[answer_col].value_counts()
#     ratio = grouped.div(total, axis=1)
#     return {group_col: ratio.round(3).to_dict(orient='index')}
#
# data = {
#     'category': ['A', 'B', 'A', 'C', 'A', 'B'],
#     'category2': ['D', 'E', 'D', 'F', 'D', 'E'],
#     'answer':   ['yes', 'no', 'yes', 'yes', 'no', 'yes']
# }
# # df = pd.DataFrame(data)
# data = {
#     'category': ['A', 'B', 'A', 'C', 'A', 'B', 'C'],
#     'answer':   ['yes', 'no', 'yes', 'yes', 'no', 'yes', 'no']
# }
#
# result = answer_ratio_by_group(data, 'category', 'answer')
# print(result)














# from ucimlrepo import fetch_ucirepo
#
# # fetch dataset
# mushroom = fetch_ucirepo(id=73)
#
# # data (as pandas dataframes)
# X = mushroom.data.features
# y = mushroom.data.targets
# print(X.head())
# print(y.head())
# # metadata
# print(mushroom.metadata)
#
# # variable information
# print(mushroom.variables)



