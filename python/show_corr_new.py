import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from .select_anchors import select_anchors


def show_corr_new(F1, X1, F2, X2, A2, K, out_file=None):
    """Visualize correspondence between two meshes."""
    col = np.array(
        [
            [0, 0, 1],
            [0, 1, 0],
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [1, 1, 0],
        ]
    )
    anum = len(col)
    P = select_anchors(A2, anum)
    sig = np.max(A2) / anum
    A2w = np.exp(-(A2 ** 2) / (2 * sig * sig))
    C2 = np.zeros((X2.shape[0], 3))
    for i in range(X2.shape[0]):
        weights = A2w[P, i]
        C2[i] = (weights[:, None] * col).sum(axis=0) / weights.sum()
    C1 = np.zeros((X1.shape[0], 3))
    for a, b in K:
        if b >= 0:
            C1[a] = C2[b]
    fig = plt.figure()
    ax = fig.add_subplot(121, projection='3d')
    poly1 = Poly3DCollection(X1[F1])
    poly1.set_facecolor(C1)
    poly1.set_edgecolor('none')
    ax.add_collection3d(poly1)
    ax.auto_scale_xyz(X1[:, 0], X1[:, 1], X1[:, 2])
    ax = fig.add_subplot(122, projection='3d')
    poly2 = Poly3DCollection(X2[F2])
    poly2.set_facecolor(C2)
    poly2.set_edgecolor('none')
    ax.add_collection3d(poly2)
    ax.auto_scale_xyz(X2[:, 0], X2[:, 1], X2[:, 2])
    if out_file:
        plt.savefig(out_file)
    else:
        plt.show()
