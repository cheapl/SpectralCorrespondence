# Spectral Correspondence for 3D Shapes

This repository contains MATLAB and Python implementations of the algorithm described in:

> V. Jain and H. Zhang, "Robust 3D Shape Correspondence in the Spectral Domain". Proceedings of the International Conference on Shape Modeling and Applications (SMI), pp. 118-129, 2006.

## MATLAB Usage

The main MATLAB entry point is `specCorr3D`:

```matlab
[K, Z, V1, V2] = specCorr3D('meshes/alien.smf', 'meshes/human.smf', 5);
```

Refer to `specCorr3D.m` or run `help specCorr3D` for parameter descriptions.

## Python Translation

A full Python rewrite is available in the `python` directory. The `spec_corr3d` function mirrors the MATLAB pipeline using NumPy and SciPy.

Example usage:

```python
from python.spec_corr3d import spec_corr3d
K, Z, V1, V2 = spec_corr3d('meshes/alien.smf', 'meshes/human.smf', k=5)
```

Running `python/main.py` performs the same test and prints matrix shapes. Ensure that `numpy`, `scipy`, and `matplotlib` are installed.
