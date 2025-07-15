import requests
class Request:
    def __init__(self, base_url):
        self.base_url = base_url

    def predict_row_request(self, row_dict):
        response = requests.post(f"{self.base_url}/predict", json=row_dict)
        print(response.status_code)
        print(response.text)

    def update_model(self, data_url):
        response = requests.get(f"{self.base_url}/update", params={"data_url":data_url})
        print(response.status_code)
        print(response.text)

    def validate_model(self):
        response = requests.get(f"{self.base_url}/validation")
        print(response.status_code)
        print(response.text)


