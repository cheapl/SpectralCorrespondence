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
A full Python translation of the MATLAB functions is available in the
``python`` folder.  The ``spec_corr3d`` function mirrors the MATLAB
``specCorr3D`` pipeline using NumPy and SciPy.

Example usage from Python:

.. code-block:: python

    from python.spec_corr3d import spec_corr3d
    K, Z, V1, V2 = spec_corr3d('meshes/alien.smf', 'meshes/human.smf', k=5)

A convenience ``python/main.py`` module runs the same test when executed
as a script.
