import numpy as np
from typing import List


def recall_at_k(labels: List[int], scores: List[float], k=5) -> float:
    ''' Recall at k '''
    labels_copy = np.array(labels)
    scores_copy = np.array(scores)

    idx = scores_copy.argsort()[::-1]

    labels_copy = labels_copy[idx]
    scores_copy = scores_copy[idx]

    scores_copy[:k] = 1
    scores_copy[k:] = 0

    tp = sum(scores_copy[scores_copy == labels_copy] == 1)
    fn = sum(scores_copy[scores_copy != labels_copy] == 0)

    return tp/(tp + fn)


def precision_at_k(labels: List[int], scores: List[float], k=5) -> float:
    ''' Precision at k '''
    labels_copy = np.array(labels)
    scores_copy = np.array(scores)

    idx = scores_copy.argsort()[::-1]

    labels_copy = labels_copy[idx]
    scores_copy = scores_copy[idx]

    scores_copy[:k] = 1
    scores_copy[k:] = 0

    tp = sum(scores_copy[scores_copy == labels_copy] == 1)
    fp = sum(scores_copy[scores_copy != labels_copy] == 1)

    return tp/(tp + fp)


def specificity_at_k(labels: List[int], scores: List[float], k=5) -> float:
    ''' Specificity at k '''
    labels_copy = np.array(labels)
    scores_copy = np.array(scores)

    idx = scores_copy.argsort()[::-1]

    labels_copy = labels_copy[idx]
    scores_copy = scores_copy[idx]

    scores_copy[:k] = 1
    scores_copy[k:] = 0

    tn = sum(scores_copy[scores_copy == labels_copy] == 0)
    fp = sum(scores_copy[scores_copy != labels_copy] == 1)

    if tn + fp == 0:
        return 0
    else:
        return tn/(tn + fp)


def f1_at_k(labels: List[int], scores: List[float], k=5) -> float:
    ''' F1-score at k '''
    recall = recall_at_k(labels, scores, k)
    precision = precision_at_k(labels, scores, k)

    if recall + precision == 0:
        return 0
    else:
        return 2 * recall * precision / (recall + precision)
