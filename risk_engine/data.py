import yfinance as yf

def download_prices(tickers, start_date, end_date):
    '''Downloads prices on Yahoo Finance'''
    data = yf.download(tickers ,start=start_date,end=end_date)
    return data.Close

def convert_to_usd(prices, fx_map):
    '''Converts prices to USD'''
    prices_usd = prices.copy()
    for asset, fx in fx_map.items():
        prices_usd[asset] = prices_usd[asset]*prices_usd[fx]
    return prices_usd