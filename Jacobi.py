from numba import njit, prange


def sum(a, x, j):
    s = 0
    for i, (m, y) in enumerate(zip(a, x)):
        if i != j:
            s += m * y
    return s


def norm(x, y):
    return max((abs(x0-y0) for x0, y0 in zip(x, y)))


def Jacobi(matrA, matrB, eps=0.001, x_init=None):
    y = [b / matrA[i][i] for i, b in enumerate(matrB)] if x_init is None else x_init.copy()

    x = [-(sum(a, y, i) - matrB[i]) / matrA[i][i] for i, a in enumerate(matrA)]

    while norm(y, x) > eps:
        for i, elem in enumerate(x):
            y[i] = elem
        for i, a in enumerate(matrA):
            x[i] = -(sum(a, y, i) - matrB[i]) / matrA[i][i]
    return x