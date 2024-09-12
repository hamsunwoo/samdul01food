from typing import Union
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "n01"}


@app.get("/food")
def food(name: str):
    #시간을 구함
    #음식 이름과 시간을 csv로 저장 -> /code/data/food.csv
    return {"food": name, "time": datetime.now()}

