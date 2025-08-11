import yfinance as yf

ticker = yf.Ticker('PINS')

# Annual cash flow (DataFrame)
cf_annual = ticker.cashflow
print("Annual Cash Flow:")
print(cf_annual)

# Quarterly cash flow (DataFrame)
cf_quarterly = ticker.quarterly_cashflow
print("\nQuarterly Cash Flow:")
print(cf_quarterly)

print()
print(type(cf_quarterly))
