from  request import Request
class Menu:
    def __init__(self):
        self.request = Request('http://127.0.0.1:8080')

    def menu(self):
        flag = True
        while flag:
            match input('Choose one of the options below: \n1. Update the model \n2. Validate model \n3. Predict a row\nany key to Exit:\nEnter your choice: \n'):
                case '1':
                    data_url = input('Enter the data url: ')
                    self.request.update_model(data_url)

                case '2':
                    self.request.validate_model()
                case '3':
                    body = eval(input('enter row dict: '))
                    self.request.predict_row_request(body)
                case _:
                    flag = False
a = Menu()
a.menu()

# C:/Users/HOME/OneDrive/שולחן העבודה/data python/buy_computer_data.csv
# {'age': '<=30', 'income':'medium','student': 'yes','credit_rating':'fair'}