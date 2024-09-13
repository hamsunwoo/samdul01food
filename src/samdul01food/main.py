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
    import os

    time = datetime.now()
    home_dir = os.path.expanduser('~')
    path = os.path.join(home_dir, "data")
    df = pd.DataFrame([[name, time]], columns=['food','time'])
    df.to_csv(f'{path}/food.csv', mode='a', index=False)
    return {"food": name, "time": datetime.now()}
