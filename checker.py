class Checker:
    def __init__(self, coached_dict):
        self.coached_dict = coached_dict

    def get_values_prediction(self):
        dict_prediction = {}
        for col in self.coached_dict.keys():
            if col == 'classified':
                continue
            dict_prediction[col] = input(f'enter the value for {col}')
        return dict_prediction

    def prediction(self, dict_prediction=None):
        if dict_prediction is None:
            dict_prediction = self.get_values_prediction()
        classified_dict = {}
        for k,v in self.coached_dict['classified'].items():
            classified_dict[k] = v
        for k, v in dict_prediction.items():
            for classified in self.coached_dict['classified'].keys():
                classified_dict[classified] *= self.coached_dict[k][v][classified]
        return max(classified_dict.items(), key=lambda x: x[1])
