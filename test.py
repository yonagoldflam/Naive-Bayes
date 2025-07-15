from manager import Manager
import uvicorn as uv
from fastapi import FastAPI


manager = Manager()
app = FastAPI()


@app.get("/update")
def update(data_url: str):
    manager.update_model(data_url)
    return {'data_url': data_url}

@app.get("/validation")
def validation():
    return {'validate resalt': manager.validate_model()}
@app.post("/predict")
def predict(vector: dict[str, str]):
    return {'resalt':(manager.predict(vector),vector)}


if __name__ == '__main__':
    uv.run('test:app', host='127.0.0.1', port=8080,reload=True)
