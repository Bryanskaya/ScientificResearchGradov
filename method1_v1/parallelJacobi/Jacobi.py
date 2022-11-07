from numba import njit, prange
from numba.typed import List, Dict
import numpy as np


@njit
def sum(strMatrA: Dict, x: np.ndarray, i: int) -> float:
    s = -strMatrA[i] * x[i]
    for j in strMatrA.keys():
        s += strMatrA[j] * x[j]
    return s


@njit
def isComplete(vectX, vectXPrev, eps):
    for i in prange(len(vectX)):
        if abs(vectX[i] - vectXPrev[i]) > eps:
            return True
    return False


@njit(parallel=True)
def Jacobi(matrA: List[Dict], vectB: np.ndarray, eps=0.001):
    # vectXPrev = [b / matrA[i][i] for i, b in enumerate(vectB)] if x_init is None else x_init.copy()
    # vectXPrev = List([0.0] * len(vectB) if x_init is None else x_init.copy())
    # vectXPrev = List([0.0] * len(vectB))
    vectXPrev = np.full(len(vectB), vectB[0], dtype=np.float64)

    vectX = np.zeros(len(vectB), dtype=np.float64)
    for i in prange(len(vectB)):
        vectX[i] = (vectB[i] - sum(matrA[i], vectXPrev, i)) / matrA[i][i]

    while isComplete(vectX, vectXPrev, eps):
        vectXPrev = vectX.copy()
        for i in prange(len(vectB)):
            vectX[i] = (vectB[i] - sum(matrA[i], vectXPrev, i)) / matrA[i][i]
    return vectX
