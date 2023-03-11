import numpy as np
from typing import List


def normalized_dcg(relevance: List[float], k: int, method: str = "standard") -> float:
    """Normalized Discounted Cumulative Gain.

    Parameters
    ----------
    relevance : `List[float]`
        Video relevance list
    k : `int`
        Count relevance to compute
    method : `str`, optional
        Metric implementation method, takes the values
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
    ideal_relevances = np.array(sorted(relevance, reverse=True)[:k])

    if method == 'standard':
        dcg = np.sum(relevances/weights)
        idcg = np.sum(ideal_relevances/weights)

        return dcg/idcg
    
    elif method == 'industry':
        relevances = np.array([2**i - 1 for i in relevances])
        ideal_relevances = np.array([2**i - 1 for i in ideal_relevances])

        dcg = np.sum(relevances/weights)
        idcg = np.sum(ideal_relevances/weights)

        return dcg/idcg
    
    else:
        raise ValueError
