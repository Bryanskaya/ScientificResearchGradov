from numba import njit, prange
from numba.typed import List
import numpy as np


@njit
def sum(strMatrA: List, x: List, i: int) -> float:
    s = -strMatrA[i] * x[i]
    for j in prange(strMatrA.shape[0]):
        s += strMatrA[j] * x[j]
    return s


@njit
def isComplete(vectX, vectXPrev, eps):
    for i in prange(len(vectX)):
        if abs(vectX[i] - vectXPrev[i]) > eps:
            return True
    return False


@njit(parallel=True)
def Jacobi(matrA: np.ndarray, vectB: np.ndarray, eps=0.001):
    # vectXPrev = [b / matrA[i][i] for i, b in enumerate(vectB)] if x_init is None else x_init.copy()
    # vectXPrev = List([0.0] * len(vectB) if x_init is None else x_init.copy())
    # vectXPrev = List([0.0] * len(vectB))
    vectXPrev = np.full(len(vectB), vectB[0], dtype=np.float64)

    vectX = np.zeros(len(matrA), dtype=np.float64)
    for i in prange(len(matrA)):
        vectX[i] = (vectB[i] - sum(matrA[i], vectXPrev, i)) / matrA[i][i]

    while isComplete(vectX, vectXPrev, eps):
        vectXPrev = vectX.copy()
        for i in prange(len(matrA)):
            vectX[i] = (vectB[i] - sum(matrA[i], vectXPrev, i)) / matrA[i][i]
    return vectX
