# Spectral Correspondence

This repository provides MATLAB code and a Python translation for the paper **Robust 3D Shape Correspondence in the Spectral Domain**.

> V. Jain and H. Zhang, *Robust 3D Shape Correspondence in the Spectral Domain*. Proceedings of the International Conference on Shape Modeling and Applications (SMI), pp. 118-129, 2006.

## MATLAB usage

The main function for the spectral correspondence code is `specCorr3D`.

```matlab
[K, Z, V1, V2] = specCorr3D('meshes/alien.smf', 'meshes/human.smf', 5);
```

For a description of the input and output parameters, see `help specCorr3D` or the file `specCorr3D.m`.

## Python translation

A full Python translation of the MATLAB functions is available in the `python` folder. The function `spec_corr3d` mirrors the MATLAB `specCorr3D` pipeline using NumPy and SciPy.

Example usage:

```python
K, Z, V1, V2 = spec_corr3d('meshes/alien.smf', 'meshes/human.smf', k=5)
```

Executing `python/main.py` will run the same test script.

