def _validate_confidence(confidence):
    '''Check that confidence level is strictly between 0 and 1'''
    x = 1 - confidence
    if x <= 0:
        raise ValueError("Confidence level must be below 1")
    if x >= 1: 
        raise ValueError("Confidence level must be >0")

    
def historical_var(returns, confidence, value):
    '''Finds the historical VaR with quantile function and returns a positive dollar value'''
    _validate_confidence(confidence)
    quantile_level = 1 - confidence 
    quantile_return = returns.quantile(quantile_level)
    return quantile_return * value * (-1) 


def historical_es(returns, confidence, value):
    '''Takes all the values below or equal to VaR and returns an average positive dollar value'''
    _validate_confidence(confidence)
    quantile_level = 1- confidence
    tail_returns = returns[returns <= returns.quantile(quantile_level)] 
    return tail_returns.mean()*value*-1 


