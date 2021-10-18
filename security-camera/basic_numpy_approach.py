# coding: utf-8
# ---------------------------------------------------------------------------- #
#                               Numpy ^2 Examples                             #
# ---------------------------------------------------------------------------- #
import numpy as np

A = np.ones ((3, 3))
B = np.zeros((3, 3 ))

s = 0
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        #  ! SSE
        s += (A[i,j] - B[i,j]) ** 2 # raise to ^2
print(s)
# ! Numpy approach
print(((A-B) **2 )) 
print(((A-B) ** 2).sum())
        