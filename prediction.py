import json


class Checker:
    def __init__(self, trained_dict):
        self.coached_dict = trained_dict
        # if self.coached_dict is None:
        #     self.read_trained_dict()

    # def read_trained_dict(self):
    #     with open(f'model files/{model_name}.json', 'r') as file:
    #         self.coached_dict = json.load(file)

    def prediction(self, row_dict):
        classified_dict = {}
        for k,v in self.coached_dict['classified'].items():
            classified_dict[k] = v
        for k, v in row_dict.items():
            for classified in self.coached_dict['classified'].keys():
                classified_dict[classified] *= self.coached_dict[k][v][classified]
        return max(classified_dict.items(), key=lambda x: x[1])
