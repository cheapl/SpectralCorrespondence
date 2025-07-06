import numpy as np


def select_anchors(A, num):
    if num < 1:
        return np.array([], dtype=int)
    n = A.shape[0]
    P = np.zeros(num, dtype=int)
    tmp = np.sum(A, axis=1)
    P[0] = np.argmax(tmp)
    if num == 1:
        return P
    P[1] = np.argmax(A[P[0]])
    for i in range(num - 2):
        sums = np.sum(A[P[: i + 2]], axis=0)
        P[i + 2] = np.argmax(sums)
    return P
