import pandas as pd

from risk_engine.data import download_prices, convert_to_usd
from risk_engine.portfolio import compute_returns, compute_portfolio_returns
from risk_engine.risk import historical_var, historical_es


fx_map = {"BNP.PA": "EURUSD=X", "0700.HK": "HKDUSD=X", "NESN.SW": "CHFUSD=X"}
weights = pd.Series({
    "SPY": 0.25,
    "TSM": 0.15,
    "BNP.PA": 0.15,
    "GLD": 0.15,
    "0700.HK": 0.10,
    "XOM": 0.10,
    "NESN.SW": 0.10,
    "EURUSD=X": -0.15,
})
portfolio_value = 1000000
start = "2016-01-01"
end = "2026-11-05"


def main():
    tickers = list(set(list(weights.index) + list(fx_map.values())))
    prices = download_prices(tickers, start_date=start, end_date=end)
    prices_usd = convert_to_usd(prices, fx_map)
    returns = compute_returns(prices_usd)
    portfolio_returns = compute_portfolio_returns(returns, weights)

    for confidence in [0.95, 0.975, 0.99]:
        var = historical_var(portfolio_returns, confidence, portfolio_value)
        es = historical_es(portfolio_returns, confidence, portfolio_value)
        print(f"{confidence:.1%} | VaR : {var:,.0f} USD | Expected Shortfall : {es:,.0f} USD")


if __name__ == "__main__":
    main()