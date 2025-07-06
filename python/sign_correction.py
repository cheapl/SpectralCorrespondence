import numpy as np
from .compute_matching import compute_matching


def sign_correction(V1, V2):
    """Align signs of eigenvectors."""
    n1, k = V1.shape
    for i in range(k):
        Z = np.linalg.norm(V1[:, : i + 1][:, None, :] - V2[:, : i + 1][None, :, :], axis=2)
        _, cost1 = compute_matching(Z)
        V2[:, i] *= -1
        Z = np.linalg.norm(V1[:, : i + 1][:, None, :] - V2[:, : i + 1][None, :, :], axis=2)
        _, cost2 = compute_matching(Z)
        if cost1 <= cost2:
            V2[:, i] *= -1
    return V2
