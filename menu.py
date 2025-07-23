from  request import Request
class Menu:
    def __init__(self):
        self.request = Request('http://127.0.0.1:8080')
        self.row_request = Request('http://127.0.0.1:8081')

    def menu(self):
        flag = True
        while flag:
            match input('Choose one of the options below: \n1. Update the model \n2. Validate model \n3. Predict a row\nany key to Exit:\n4. select data for prediction \nEnter your choice: \n'):
                case '1':
                    data_url = input('Enter the data url: ')
                    self.request.update_model(data_url)

                case '2':
                    self.request.validate_model()
                case '3':
                    body = eval(input('enter row dict: '))
                    self.request.predict_row_request(body)

                case '4':
                    data_name = input('Enter the data name: ')
                    self.request.select_data(data_name)

                case '5':
                    self.request.get_trained_model()

                case '6':
                    body = eval(input('enter row dict: '))
                    self.row_request.classify_row_request(body)

                case _:
                    flag = False
a = Menu()
a.menu()

# C:/Users/HOME/OneDrive/שולחן העבודה/data python/buy_computer_data.csv
# {'age': '<=30', 'income':'medium','student': 'yes','credit_rating':'fair'}
# C:/Users/HOME/OneDrive/שולחן העבודה/data python/PythonProject3/models/buy_computer_data.csv