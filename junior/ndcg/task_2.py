import numpy as np
from typing import List


def discounted_cumulative_gain(relevance: List[float], k: int, method: str = "standard") -> float:
    """Discounted Cumulative Gain

    Parameters
    ----------
    relevance : `List[float]`
        Video relevance list
    k : `int`
        Count relevance to compute
    method : `str`, optional
        Metric implementation method, takes the values​​
        `standard` - adds weight to the denominator
        `industry` - adds weights to the numerator and denominator
        `raise ValueError` - for any value

    Returns
    -------
    score : `float`
        Metric score
    """
    weights = np.log2(np.arange(2, k + 2))
    relevances = np.array(relevance[:k])
    
    if method == 'standard':
        score = np.sum(relevances/weights)

    elif method == 'industry':
        relevances = np.array([2**i - 1 for i in relevances])
        score = np.sum(relevances/weights)

    else:
        raise ValueError
    
    return score
