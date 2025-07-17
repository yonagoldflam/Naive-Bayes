class Checker:
    def __init__(self, coached_dict):
        self.coached_dict = coached_dict

    def prediction(self, row_dict):
        classified_dict = {}
        for k,v in self.coached_dict['classified'].items():
            classified_dict[k] = v
        for k, v in row_dict.items():
            for classified in self.coached_dict['classified'].keys():
                classified_dict[classified] *= self.coached_dict[k][v][classified]
        return max(classified_dict.items(), key=lambda x: x[1])
