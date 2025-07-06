import numpy as np
from .compute_matching import compute_matching


def compute_improved_matching(S, A1, A2, anc_num):
    """Matching with anchors as in MATLAB computeImprovedMatching."""
    S = S.astype(float)
    n1, n2 = S.shape
    S = S / np.max(np.abs(S))
    idx = np.zeros((anc_num, 2), dtype=int)
    Sim = [S.copy()]
    for a in range(anc_num):
        min_pos = np.unravel_index(np.argmin(S), S.shape)
        idx[a] = min_pos
        S[min_pos] = np.inf
        fvec1 = A1[min_pos[0]] / np.max(A1[min_pos[0]])
        fvec2 = A2[min_pos[1]] / np.max(A2[min_pos[1]])
        for i in range(n1):
            S[i] -= (fvec1[i] + fvec2) / 2
        sim = (fvec1[:, None] - fvec2[None, :]) ** 2
        sim = sim / np.max(sim)
        Sim.append(sim)
    S = Sim[0]
    for a in range(anc_num):
        S = S + Sim[a + 1]
    K, cost = compute_matching(S)
    return K, S, idx, float(cost)
