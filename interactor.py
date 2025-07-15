import pandas as pd

class Interactor:
    def __init__(self, url):
        self.df = self.get_data(url)

    def get_data(self, url):
        if url[-3:] == 'csv':
            return pd.read_csv(url,encoding='utf-8')
        else:
            return None



