import numpy as np
from .read_smf import read_smf
from .construct_geodesic import construct_geodesic
from .apply_gaussian import apply_gaussian
from .eig_sorted import eig_sorted
from .sign_correction import sign_correction
from .exhaustive_reorder import exhaustive_reorder
from .tps import tps
from .compute_improved_matching import compute_improved_matching
from .compute_matching import compute_matching
from .show_corr_new import show_corr_new



def spec_corr3d(file1, file2, k=5):
    F1, X1 = read_smf(file1)
    F2, X2 = read_smf(file2)

    A1 = construct_geodesic(F1, X1)
    A2 = construct_geodesic(F2, X2)

    G1 = apply_gaussian(A1)
    G2 = apply_gaussian(A2)


    V1, D1 = eig_sorted(G1, 'd', k)
    V2, D2 = eig_sorted(G2, 'd', k)


    for i in range(k):
        V1[:, i] *= np.sqrt(abs(D1[i, i]))
        V2[:, i] *= np.sqrt(abs(D2[i, i]))


    V2 = sign_correction(V1[:, :k], V2[:, :k])
    V2 = exhaustive_reorder(V1, V2, k)

    _, _, _, V2[:, 1:k] = tps(V1[:, 1:k], V2[:, 1:k])


    Z = np.zeros((V1.shape[0], V2.shape[0]))
    for i in range(1, k):
        diff = V1[:, i][:, None] - V2[:, i][None, :]
        Z += diff ** 2
    Z = np.sqrt(Z)


    for anum in range(6):
        K, _, _, cost = compute_improved_matching(Z, A1, A2, anum)
    show_corr_new(F1, X1, F2, X2, A2, K)

    return K, Z, V1, V2
