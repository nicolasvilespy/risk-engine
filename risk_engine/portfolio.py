import numpy as np

def compute_returns(prices):
    '''Compute daily returns based on closing prices'''
    returns = prices.dropna().pct_change().dropna()
    return returns

def compute_portfolio_returns(returns, weights):
    '''Compute portfolio returns by taking into account the weight of each asset'''
    portfolio_returns = (returns[weights.index] * weights).sum(axis=1)
    return portfolio_returns








