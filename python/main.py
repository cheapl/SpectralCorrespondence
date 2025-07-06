import os
import sys

if __name__ == '__main__' and __package__ is None:
    # When executed directly, ensure the project root is on sys.path so that
    # imports using the package name ``python`` work correctly. This allows
    # modules like ``spec_corr3d`` to resolve their relative imports.
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.insert(0, repo_root)
    from python.spec_corr3d import spec_corr3d
else:
    from .spec_corr3d import spec_corr3d


def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    mesh1 = os.path.join(repo_root, 'meshes', 'alien.smf')
    mesh2 = os.path.join(repo_root, 'meshes', 'human.smf')
    K, Z, V1, V2 = spec_corr3d(mesh1, mesh2, k=5)
    print('K shape:', K.shape)
    print('Z shape:', Z.shape)
    print('V1 shape:', V1.shape)
    print('V2 shape:', V2.shape)


if __name__ == '__main__':
    main()
