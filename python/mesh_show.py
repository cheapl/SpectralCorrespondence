import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def mesh_show(M, show_edges=False):
    vertices = np.asarray(M['vertices'])
    faces = np.asarray(M['faces'])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    poly = Poly3DCollection(vertices[faces])
    poly.set_facecolor('red')
    poly.set_edgecolor('k' if show_edges else 'none')
    ax.add_collection3d(poly)
    ax.auto_scale_xyz(vertices[:, 0], vertices[:, 1], vertices[:, 2])
    return poly
