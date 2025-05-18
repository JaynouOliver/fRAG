from typing import Union
from eodhdh import get_eodhdh_data
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/eodhdh")
def get_eodhdh_data_route():
    return get_eodhdh_data()








#sampple postman request
