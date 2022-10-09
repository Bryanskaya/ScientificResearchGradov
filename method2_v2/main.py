import random
import time

import numpy as np

from numba import njit, prange

from configParams import *
from monte_carlo import isBorder, monte_carlo, uBorder
from visualizer import draw2D


def to(i, j=0):
    """ Transform real coordinates to matrix's A coordinates """
    return n * i + j


@njit
def isHole(i, j):
    if holeI < i < holeI + holeM and \
            holeJ < j < holeJ + holeN:
        return True
    return False


@njit
def getMatrix():
    matrA = np.zeros((m, n))

    for i in prange(m):
        matrA[i][0] = u0Left                    # left
        matrA[i][n - 1] = u0Right               # right
    for i in prange(n):
        matrA[0][i] = u0Top                     # top
        matrA[m - 1][i] = u0Bottom              # bottom

    for i in prange(m):
        for j in prange(n):
            if isHole(i, j):
                matrA[i][j] = np.nan
                continue
            if isBorder(i, j):
                matrA[i][j] = uBorder(i, j)
                continue

    return matrA


def main():
    random.seed()

    matrA = getMatrix()
    start = time.time()
    matrU = monte_carlo(matrA)
    print("Time: ", time.time() - start)
    draw2D(matrU)


if __name__ == '__main__':
    main()