import numpy as np


def read_smf(fname):
    """Read a simple SMF mesh file.

    Parameters
    ----------
    fname : str
        Path to the SMF file.

    Returns
    -------
    F : ndarray of shape (m, 3)
        Face indices starting at zero.
    X : ndarray of shape (n, 3)
        Vertex coordinates.
    """
    vertices = []
    faces = []
    with open(fname, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('v'):
                parts = line.split()
                if len(parts) >= 4:
                    vertices.append([float(parts[1]), float(parts[2]), float(parts[3])])
            elif line.startswith('f'):
                parts = line.split()
                if len(parts) >= 4:
                    faces.append([int(parts[1]) - 1, int(parts[2]) - 1, int(parts[3]) - 1])
    X = np.array(vertices, dtype=float)
    F = np.array(faces, dtype=int)
    return F, X
