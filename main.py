from interactor import Interactor
from coach import Coach
from checker import Checker

interact = Interactor()
coach = Coach(interact.df)
checker = Checker(coach.coached_dict)
print(checker.prediction())
