class Classifier:
    def __init__(self):
        pass

    def classifier(self,trained_dict, row_dict):
        classified_dict = {}
        for k,v in trained_dict['classified'].items():
            classified_dict[k] = v
        for k, v in row_dict.items():
            for classified in trained_dict['classified'].keys():
                classified_dict[classified] *= trained_dict[k][v][classified]
        return max(classified_dict.items(), key=lambda x: x[1])
