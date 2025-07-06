import numpy as np


def compute_pairwise(X):
    """Compute pairwise Euclidean distances."""
    X = np.asarray(X, dtype=float)
    diff = X[:, None, :] - X[None, :, :]
    return np.sqrt(np.sum(diff ** 2, axis=-1))
