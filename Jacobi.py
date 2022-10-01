# from numba import njit, prange


def sum(strMatrA, x, i):
    s = - strMatrA[i] * x[i]
    for j in range(len(strMatrA)):
        s += strMatrA[j] * x[j]
    return s


def norm(x, y):
    maxDiff = 0
    for i in range(len(x)):
        maxDiff = max(maxDiff, abs(x[i] - y[i]))
    return maxDiff


def Jacobi(matrA, vectB, eps=0.001, x_init=None):
    # y = [b / matrA[i][i] for i, b in enumerate(vectB)] if x_init is None else x_init.copy()
    y = [0] * len(vectB) if x_init is None else x_init.copy()

    x = []
    for i in range(len(matrA)):
        x.append(-(sum(matrA[i], y, i) - vectB[i]) / matrA[i][i])

    print(len(y), len(matrA), len(x))
    while norm(y, x) > eps:
        y = x.copy()
        for i in range(len(matrA)):
            x[i] = (vectB[i] - sum(matrA[i], y, i)) / matrA[i][i]
    return x