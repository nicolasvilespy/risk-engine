import pandas as pd
import pytest

from risk_engine.risk import historical_var, historical_es
from risk_engine.data import convert_to_usd

returns = pd.Series([-0.04, -0.02, -0.01, 0.01, 0.03])
returns_2 = pd.Series([-0.05, -0.03, -0.02, -0.01, -0.005, 0, 0.005, 0.01, 0.02, 0.03])
portfolio_value = 1000000

def test_var_returns():
    result = historical_var(returns, 0.75, portfolio_value)
    assert result == pytest.approx(20000)

def test_es_returns():
    result = historical_es(returns, 0.75, portfolio_value)
    assert result == pytest.approx(30000)

def test_var_returns_2():
    result = historical_var(returns_2, 0.80, portfolio_value)
    assert result == pytest.approx(22000)

def test_es_returns_2():
    result = historical_es(returns_2, 0.8, portfolio_value)
    assert result == pytest.approx(40000)

def test_valerr_0():
    with pytest.raises(ValueError):
        historical_var(returns, 0, portfolio_value)

def test_valerr_1():
    with pytest.raises(ValueError):
        historical_var(returns, 1, portfolio_value)

def test_conversion():
    test_prices = pd.DataFrame({"AAA": [10.0], "EURUSD=X": [1.2]})
    result = convert_to_usd(test_prices, {"AAA": "EURUSD=X"})
    assert result["AAA"].iloc[0] == pytest.approx(12)
