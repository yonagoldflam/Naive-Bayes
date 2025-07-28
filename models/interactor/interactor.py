import pandas as pd
from pathlib import Path

class Interactor:
    def __init__(self):
        self.df = None
        self.current_model = None
        self.file_name = None

    def get_data(self, url):
        if url[-3:] == 'csv':
            self.df = pd.read_csv(f"data/{url}",encoding='utf-8')
        self.file_name = Path(url).stem






