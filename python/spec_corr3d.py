import numpy as np
from scipy.linalg import eigh
from .read_smf import read_smf
from .construct_geodesic import construct_geodesic
from .apply_gaussian import apply_gaussian
from .compute_matching import compute_matching


def eig_sorted(A, k):
    vals, vecs = eigh(A)
    idx = np.argsort(-vals)
    vals = vals[idx][:k]
    vecs = vecs[:, idx][:, :k]
    return vecs, np.diag(vals)


def spec_corr3d(file1, file2, k=5):
    F1, X1 = read_smf(file1)
    F2, X2 = read_smf(file2)

    A1 = construct_geodesic(F1, X1)
    A2 = construct_geodesic(F2, X2)

    G1 = apply_gaussian(A1)
    G2 = apply_gaussian(A2)

    V1, D1 = eig_sorted(G1, k)
    V2, D2 = eig_sorted(G2, k)

    for i in range(k):
        V1[:, i] *= np.sqrt(abs(D1[i, i]))
        V2[:, i] *= np.sqrt(abs(D2[i, i]))

    Z = np.zeros((V1.shape[0], V2.shape[0]))
    for i in range(1, k):
        diff = V1[:, i][:, None] - V2[:, i][None, :]
        Z += diff ** 2
    Z = np.sqrt(Z)

    K, cost = compute_matching(Z)
    return K, Z, V1, V2
