import random
import numpy as np

from configParams import *
from monte_carlo import isBorder, monte_carlo, uBorder
from visualizer import draw2D


def to(i, j=0):
    """ Transform real coordinates to matrix's A coordinates """
    return n * i + j


def isHole(i, j):
    if holeI < i < holeI + holeM and \
            holeJ < j < holeJ + holeN:
        return True
    return False


def borderTemperature(i, j):
    if i == holeI: return u0TopInside
    if i == holeI + holeM: return u0BottomInside
    if j == holeJ: return u0LeftInside
    if j == holeJ + holeN: return u0RightInside
    print("*****", i, j)


def getMatrix():
    matrA = np.zeros((m, n))

    for i in range(m):
        matrA[i][0] = u0Left                    # left
        matrA[i][n - 1] = u0Right               # right
    for i in range(n):
        matrA[0][i] = u0Top                     # top
        matrA[m - 1][i] = u0Bottom              # bottom

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if isHole(i, j):
                matrA[i][j] = None
                continue
            if isBorder(i, j):
                matrA[i][j] = uBorder(i, j)
                continue

    return matrA


def main():
    random.seed()

    matrA = getMatrix()
    matrU = monte_carlo(matrA)
    draw2D(matrU)


if __name__ == '__main__':
    main()