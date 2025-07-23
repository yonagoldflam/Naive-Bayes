import requests


class Request:
    def __init__(self, base_url):
        self.base_url = base_url

    def classify_row_request(self, row_dict):
        response = requests.post(f"{self.base_url}/classify", json=row_dict)
        print(response.status_code)
        print(response.text)

    def predict_row_request(self, row_dict):
        response = requests.post(f"{self.base_url}/predict", json=row_dict)
        print(response.status_code)
        print(response.text)

    def update_model(self, data_url):
        response = requests.get(f"{self.base_url}/update", params={"data_url": data_url})
        print(response.status_code)
        print(response.text)

    def validate_model(self):
        response = requests.get(f"{self.base_url}/validation")
        print(response.status_code)
        print(response.text)

    def get_trained_model(self):
            response = requests.get(f"{self.base_url}/trained")
            print(response.status_code)
            print(response.text)

    def select_data(self,model_name):
        response = requests.get(f"{self.base_url}/select", params={"model_name": model_name})
        print(response.status_code)
        print(response.text)







#   curl -X POST http://127.0.0.1:8081/classify \-H "Content-Type: application/json" \-d "{\"age\": \"<=30\", \"income\": \"medium\", \"student\": \"yes\", \"credit_rating\": \"fair\"}"