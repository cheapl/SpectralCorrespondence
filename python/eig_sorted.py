import numpy as np
from scipy.linalg import eigh


def eig_sorted(A, order='d', k=None):
    """Eigen decomposition with sorted eigenvalues."""
    A = np.asarray(A, dtype=float)
    vals, vecs = eigh(A)
    idx = np.argsort(vals)
    if order == 'd':
        idx = idx[::-1]
    vals = vals[idx]
    vecs = vecs[:, idx]
    if k is not None:
        vals = vals[:k]
        vecs = vecs[:, :k]
    return vecs, np.diag(vals)
