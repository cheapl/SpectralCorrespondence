
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


