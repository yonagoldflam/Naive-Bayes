import pandas as pd
from pathlib import Path

class Interactor:
    def __init__(self):
        self.df = None
        self.current_model = None
        self.file_name = None

    def get_data(self, url):
        url = "buy_computer_data.csv"
        if url[-3:] == 'csv':
            self.df = pd.read_csv(url,encoding='utf-8')
        self.file_name = Path(url).stem






