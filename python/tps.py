import numpy as np
from .compute_pairwise import compute_pairwise


def _find_phi(Y):
    n, dim = Y.shape
    phi = np.zeros((n, n))
    for i in range(dim):
        diff = Y[:, i][:, None] - Y[:, i][None, :]
        phi += diff ** 2
    return -np.sqrt(phi)


def _non_rigid_transform(v, d, w, phi):
    K, dim = v.shape
    v_aug = np.hstack([v, np.ones((K, 1))])
    fv = v_aug.dot(d) + phi.dot(w)
    return fv[:, :dim]


def _update_M(X, V):
    n, dim = V.shape
    m = X.shape[0]
    diff = V[:, None, :] - X[None, :, :]
    S = np.sum(diff ** 2, axis=2)
    M = np.zeros((n, m))
    idx = np.argmin(S, axis=1)
    M[np.arange(n), idx] = 1
    return M


def _update_transform(X, V, M, d, w, lam, dim, phi):
    N = X.shape[0]
    K = V.shape[0]
    Y = (M.dot(X)) / M.sum(axis=1)[:, None]
    Y_aug = np.hstack([Y, np.ones((K, 1))])
    V_aug = np.hstack([V, np.ones((K, 1))])
    phi_l = phi + lam * np.eye(K)
    A = np.block([[phi_l, V_aug], [V_aug.T, np.zeros((dim + 1, dim + 1))]])
    b = np.vstack([Y_aug, np.zeros((dim + 1, dim))])
    sol = np.linalg.lstsq(A, b, rcond=None)[0]
    w[:] = sol[:K]
    d[:] = sol[K:]
    return d, w


def tps(X, V, F1=None, F2=None, iters=10):
    N = X.shape[0]
    K = V.shape[0]
    lam = (np.sum(compute_pairwise(V)) / (K * K)) ** 2
    dim = X.shape[1]
    V_init = V.copy()
    phi = _find_phi(V_init)
    M = np.ones((N, K))
    d = np.eye(dim + 1)
    w = np.zeros((K, dim + 1))
    for _ in range(iters):
        V = _non_rigid_transform(V_init, d, w, phi)
        M = _update_M(X, V)
        d, w = _update_transform(X, V_init, M, d, w, lam, dim, phi)
        lam = (np.sum(compute_pairwise(V)) / (K * K)) ** 2
    V = _non_rigid_transform(V_init, d, w, phi)
    return w, d, M, V
