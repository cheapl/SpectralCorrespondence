import numpy as np
from scipy.sparse.csgraph import dijkstra


def construct_geodesic(F, X):
    """Approximate geodesic distances using graph distances."""
    X = np.asarray(X, dtype=float)
    F = np.asarray(F, dtype=int)
    n = X.shape[0]
    dim = X.shape[1]

    adj = np.zeros((n, n), dtype=float)
    for face in F:
        i, j, k = face
        adj[i, j] = adj[j, i] = 1
        adj[j, k] = adj[k, j] = 1
        adj[k, i] = adj[i, k] = 1

    A = np.zeros((n, n), dtype=float)
    for i in range(dim):
        diff = X[:, i][:, None] - X[:, i][None, :]
        A += diff ** 2
    A = np.sqrt(A)
    A *= adj
    A[A == 0] = np.inf
    np.fill_diagonal(A, 0)

    dist_matrix = dijkstra(A, directed=False)
    return dist_matrix
