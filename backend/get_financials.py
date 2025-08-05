import json
import requests
from dotenv import load_dotenv
import os
import csv


def load_json_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def save_json_to_file(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def get_tickers():
    csv_path = "../stock_tickers.csv"
    tickers = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            # Assuming ticker symbol is in first column; adjust if needed
            tickers.append(row[0].strip())
    return tickers






def get_stock_data(offset,tickers):
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    
    #symbol_string = ",".join(tickers)
    #url = f'https://financialmodelingprep.com/api/v3/quote/{symbol_string}?apikey={API_KEY}'
    symbol = "AAPL"
    #url = f"https://financialmodelingprep.com/api/v3/profile/{symbol}?apikey={API_KEY}"
    url = f"https://financialmodelingprep.com/api/v3/ratios/AAPL?apikey={API_KEY}"

    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status {response.status_code}")
        return []

def get_financials():
    json_path = "../meta_data.json"
    json_data = load_json_from_file(json_path)
    offset = json_data["offset"]
    tickers = get_tickers()
    batch_tickers = tickers[offset:min(offset+5, len(tickers))]
    print(batch_tickers)
    print(get_stock_data(offset,batch_tickers))
    #json_data["offset"]+=100
    #save_json_to_file(json_path, json_data)

if __name__  == "__main__":
    get_financials()