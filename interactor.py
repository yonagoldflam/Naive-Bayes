import pandas as pd

class Interactor:
    def __init__(self):
        self.df = self.get_data()

    def get_data(self):
        while (True):
            match input('press 1 to csv file or press 0 to exit'):
                case '1':
                    df = pd.read_csv(input('enter file name and path: '))
                    return df
                case '0':
                    return None
                case _:
                    print('please enter a valid file name')


