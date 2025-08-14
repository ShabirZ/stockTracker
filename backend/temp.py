import yfinance as yf

ticker = yf.Ticker('PINS')
class stock_financials:
    def __init__(self, stock_ticker):
        self.stock_ticker = stock_ticker
        self.free_cashflow_4_quarters = 0 
        self.yearly_cf = 0
        self.get_free_cash_flow()

    def get_free_cash_flow(self):
        cf_annual = ticker.cashflow
    
        print(f"Annual Cash Flow: {self.stock_ticker}")
        recent_year_cf = cf_annual.iloc[:, 0]["Free Cash Flow"]
        print(recent_year_cf)

        # Quarterly cash flow (DataFrame)
        cf_quarterly = ticker.quarterly_cashflow
        last_4_quarter_cashflow = 0

        total_quarters = len(cf_quarterly.columns)
        for i in range(min(total_quarters,4)):
            if cf_quarterly[cf_quarterly.columns[i]]["Free Cash Flow"]:
                last_4_quarter_cashflow += cf_quarterly[cf_quarterly.columns[i]]["Free Cash Flow"]
        self.yearly_cf = recent_year_cf
        self.free_cashflow_4_quarters = last_4_quarter_cashflow
        print(self.yearly_cf, self.free_cashflow_4_quarters)
        return [last_4_quarter_cashflow, cf_annual]
pinterest_sample = stock_financials("PINS")
print(pinterest_sample.free_cashflow)
