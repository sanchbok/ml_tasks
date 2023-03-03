import numpy as np


def smape(y_true: np.array, y_pred: np.array) -> float:
    idx = (y_true == y_pred) & (y_true == 0)
    numerator = 2 * np.abs(y_true - y_pred)
    denominator = np.abs(y_true) + np.abs(y_pred)
    denominator[idx] = 1

    return np.mean(numerator / denominator)
