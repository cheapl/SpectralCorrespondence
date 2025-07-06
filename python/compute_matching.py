import numpy as np


def compute_matching(S):
    """Compute row-wise minimum matching cost."""
    S = np.asarray(S, dtype=float)
    indices = np.argmin(S, axis=1)
    costs = S[np.arange(S.shape[0]), indices]
    K = np.column_stack((np.arange(S.shape[0]), indices))
    total_cost = costs.sum()
    return K, float(total_cost)
