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
    K, Z, V1, V2 = spec_corr3d('../meshes/alien.smf', '../meshes/human.smf', k=5)
    print('K shape:', K.shape)
    print('Z shape:', Z.shape)
    print('V1 shape:', V1.shape)
    print('V2 shape:', V2.shape)


if __name__ == '__main__':
    main()
