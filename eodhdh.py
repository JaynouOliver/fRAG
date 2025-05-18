from eodhd import APIClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

api = APIClient(os.getenv("EODHD_API_KEY"))



def get_eodhdh_data():
    resp = api.get_eod_historical_stock_market_data(symbol = 'AAPL.MX', period='d', from_date = '2023-01-01', to_date = '2023-01-15', order='a')
    print("Printing the response")
    return resp

