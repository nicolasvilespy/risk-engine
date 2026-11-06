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