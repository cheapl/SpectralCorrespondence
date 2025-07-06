import numpy as np


def apply_gaussian(H, sigma=None):
    """Apply a Gaussian kernel to a dissimilarity matrix."""
    H = np.asarray(H, dtype=float)
    if sigma is None:
        sigma = np.max(np.abs(H))
    return np.exp((-H**2) / (2 * sigma**2))
