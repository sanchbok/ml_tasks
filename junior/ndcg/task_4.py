import numpy as np
from typing import List


def avg_ndcg(list_relevances: List[List[float]], k: int, method: str = 'standard') -> float:
    """avarage nDCG

    Parameters
    ----------
    list_relevances : `List[List[float]]`
        Video relevance matrix for various queries
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
    list_relevance = np.array(list_relevances)[:, :k]
    ideal_relevance = np.array(
        list(map(lambda x: sorted(x, reverse=True)[:k], list_relevances))
    )

    if method == 'standard':
        dcg = np.sum(list_relevance/weights, axis=1)
        idcg = np.sum(ideal_relevance/weights, axis=1)
        return np.mean(dcg/idcg)

    elif method == 'industry':
        list_relevance = np.array(
            list(map(lambda x: [2**i - 1 for i in x], list_relevance))
        )

        ideal_relevance = np.array(
            list(map(lambda x: [2**i - 1 for i in x], ideal_relevance))
        )

        dcg = np.sum(list_relevance/weights, axis=1)
        idcg = np.sum(ideal_relevance/weights, axis=1)
        return np.mean(dcg/idcg)

    else:
        raise ValueError
