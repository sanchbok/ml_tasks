import numpy as np


def turnover_error(y_true: np.array, y_pred: np.array) -> float:
    ''' Metrics penalizing more for underprediction '''
    return np.mean(((y_true - y_pred) / y_pred)**2)
