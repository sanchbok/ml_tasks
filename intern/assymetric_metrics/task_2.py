import numpy as np


def ltv_error(y_true: np.array, y_pred: np.array) -> float:
    return np.mean(((y_true - y_pred) * (y_pred + 1))**2)
