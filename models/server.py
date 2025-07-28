from manager import Manager
from validator.validator import Validator
import uvicorn as uv
from fastapi import FastAPI

validate = Validator()
manager = Manager()
app = FastAPI()

@app.get("/update")
def update(data_url: str):
    manager.update_model(data_url)
    return {'data_url': data_url}

@app.get("/validation")
def validation():
    return {'validate resalt': validate.validate_model(manager.df)}


@app.get("/select")
def select(model_name: str):
    print(model_name)
    manager.select_data(model_name)
    return {'model_name': model_name}
@app.get("/trained")
def trained():
    return manager.get_trained_model()

# if __name__ == '__main__':
#     uv.run('server:app', host='127.0.0.1', port=8040,reload=True)
