# from numba import njit, prange


def sum(strMatrA, x, i):
    s = - strMatrA[i] * x[i]
    for j in range(len(strMatrA)):
        s += strMatrA[j] * x[j]
    return s


def isComplete(vectX, vectXPrev, eps):
    for i in range(len(vectX)):
        if abs(vectX[i] - vectXPrev[i]) > eps:
            return True
    return False


def Jacobi(matrA, vectB, x_init=None, eps=0.001):
    # vectXPrev = [b / matrA[i][i] for i, b in enumerate(vectB)] if x_init is None else x_init.copy()
    vectXPrev = [0] * len(vectB) if x_init is None else x_init.copy()

    vectX = []
    for i in range(len(matrA)):
        vectX.append((vectB[i] - sum(matrA[i], vectXPrev, i)) / matrA[i][i])

    while isComplete(vectX, vectXPrev, eps):
        vectXPrev = vectX.copy()
        for i in range(len(matrA)):
            vectX[i] = (vectB[i] - sum(matrA[i], vectXPrev, i)) / matrA[i][i]
    return vectX