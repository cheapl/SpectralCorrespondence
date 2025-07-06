import numpy as np
import itertools
from .compute_matching import compute_matching


def exhaustive_reorder(E1, E2, k):
    """Reorder eigenvectors of E2 to best match E1."""
    n1 = E1.shape[0]
    n2 = E2.shape[0]
    perms = itertools.permutations(range(1, k))
    sign_options = list(itertools.product([1, -1], repeat=k - 1))
    mincost = np.inf
    best_E2 = E2.copy()
    for p in perms:
        for s in sign_options:
            temp = E2.copy()
            temp[:, 1:k] = E2[:, list(p)]
            temp[:, 1:k] *= s
            Z = np.zeros((n1, n2))
            for i in range(1, k):
                diff = E1[:, i][:, None] - temp[:, i][None, :]
                Z += diff ** 2
            Z = np.sqrt(Z)
            _, cost = compute_matching(Z)
            if cost < mincost:
                mincost = cost
                best_E2 = temp
    return best_E2
