import numpy as np
from scipy.sparse.csgraph import dijkstra


def pw_graph_dist(A):
    A = np.asarray(A, dtype=float)
    A = np.where(A < 0, np.inf, A)
    return dijkstra(A, directed=False)
