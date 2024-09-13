from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import pandas as pd

app = FastAPI()

origins = [
    "http://localhost:8899",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "n01"}


@app.get("/food")
def food(name: str):
    #시간을 구함
    #음식 이름과 시간을 csv로 저장 -> /code/data/food.csv
    return {"food": name, "time": datetime.now()}


