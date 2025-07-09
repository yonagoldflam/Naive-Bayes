from interactor import Interactor
from coach import Coach
from checker import Checker
from manager import Manager


interact = Interactor()
manage = Manager(interact.df)
manage.cat_df()
manage.coached_df()
print(manage.prediction_df())
# print(manage.df_30)
# print(manage.df_70)
# coach = Coach(interact.df)
# checker = Checker(coach.coached_dict)
# print(checker.prediction())


#  C:/Users/HOME/OneDrive/שולחן העבודה/data python/buy_computer_data.csv
#  <=30
#  medium
#  yes
#  fair