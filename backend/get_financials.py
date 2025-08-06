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






def get_stock_data(offset,curr_ticker):
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    

    #url = f"https://financialmodelingprep.com/api/v3/profile/{symbol}?apikey={API_KEY}"
    url = f"https://financialmodelingprep.com/api/v3/ratios/{curr_ticker}?apikey={API_KEY}"

    print(url)
    stock_data_json_path = "../stock_data.json"
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
    stock_dict = {}
    while True:
        if offset >= len(tickers):
            offset = 0
        curr_ticker = tickers[offset]

        offset+=1
        print(f"CURRENT TICKER : {curr_ticker}")
        print()
        print()
        curr_stock_data = get_stock_data(offset,curr_ticker)
        if not curr_stock_data:
            print(f"OFFSET {offset} BREAKING")
            break
        print(f"STOCK DATA:")
        stock_dict[curr_ticker] = curr_stock_data
        #json_data["offset"]+=100
        #save_json_to_file(json_path, json_data)
    save_json_to_file("../stock_data.json", stock_dict)
    offset_dict = {}
    offset_dict["offset"] = offset
    save_json_to_file(json_path, offset_dict["offset"])
if __name__  == "__main__":
    get_financials()