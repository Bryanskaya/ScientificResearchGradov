from collections.abc import Sequence, MutableSequence


def Jacobi(A, b, eps=0.001, x_init = None):
    def sum(a, x, j):
        S: float = 0
        for i, (m, y) in enumerate(zip(a, x)):
            if i != j:
                S += m*y
        return S

    def norm(x, y):
        return max((abs(x0-y0) for x0, y0 in zip(x, y)))

    if x_init is None:
        y = [a/A[i][i] for i, a in enumerate(b)]
    else:
        y = x_init.copy()

    x = [-(sum(a, y, i) - b[i])/A[i][i]
                      for i, a in enumerate(A)]

    while norm(y, x) > eps:
        for i, elem in enumerate(x):
            y[i] = elem
        for i, a in enumerate(A):
            x[i] = -(sum(a, y, i) - b[i])/A[i][i]
    return x