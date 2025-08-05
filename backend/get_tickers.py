import requests
from dotenv import load_dotenv
import os
import csv

def save_tickers_to_csv(tickers, csv_path, ticker_column='symbol'):
    """
    Save a list of ticker symbols to a CSV file.

    Args:
        tickers (list): List of ticker symbols (strings).
        csv_path (str): Path to the CSV file to write.
        ticker_column (str): The column name for the ticker symbols.
    """
    with open(csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[ticker_column])
        writer.writeheader()
        for ticker in tickers:
            writer.writerow({ticker_column: ticker})


def get_tickers():
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    url = f'https://financialmodelingprep.com/api/v3/stock/list?apikey={API_KEY}'

    response = requests.get(url)
    data = response.json()
    filtered_stocks = [
            item for item in data
            if item.get('type') == 'stock' and item.get('exchangeShortName') in ('NASDAQ', 'NYSE', 'AMEX')
        ]

        # Take first 5000 tickers from filtered list
    #top_5000 = filtered_stocks[:5000]

    tickers = [item['symbol'] for item in filtered_stocks]
    csv_path = "../data.csv"
    save_tickers_to_csv(tickers,csv_path, "symbol")
    print("First 10 tickers:", tickers[:10])
    print("\nRemaining tickers:", tickers[10:])




if __name__  == "__main__":
    get_tickers()