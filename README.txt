
This file describes how to use the MATLAB code for "Robust 3D Shape
Correspondence in the Spectral Domain".

    V. Jain and H. Zhang, "Robust 3D Shape Correspondence in the
    Spectral Domain". Proc. Int. Conf. on Shape Modeling and
    Applications (SMI), pp. 118-129, 2006.

The main function call for the spectral correspondence code is
"specCorr3D". Example:
    [K, Z, V1, V2] = specCorr3D('meshes/alien.smf', 'meshes/human.smf', 5);
The description of the input and output parameters can be seen with
"help specCorr3D" or referring to the file specCorr3D.m



Python translation
------------------
A partial Python implementation is available in the ``python`` folder.  The
``spec_corr3d`` function replicates the MATLAB ``specCorr3D`` pipeline using
NumPy and SciPy:

.. code-block:: python

    from python.spec_corr3d import spec_corr3d
    K, Z, V1, V2 = spec_corr3d('meshes/alien.smf', 'meshes/human.smf', k=5)

The Python version does not implement all MATLAB helper functions, but provides
basic functionality for loading SMF files, computing geodesic distances,
applying Gaussian kernels and performing a simple matching.
