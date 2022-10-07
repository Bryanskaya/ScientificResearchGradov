import random
import numpy as np

from configParams import *


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


def getMatrixA():
    stepX2 = stepX ** 2
    stepZ2 = stepZ ** 2
    tempSize = n * m
    matrA = np.zeros((tempSize, tempSize))

    for i in range(m):
        matrA[to(i)][to(i)] = 1                 # left
        matrA[to(i, n - 1)][to(i, n - 1)] = 1   # right
    for i in range(n):
        matrA[to(0, i)][to(0, i)] = 1           # top
        matrA[to(m - 1, i)][to(m - 1, i)] = 1   # bottom

    stepX2Inv = 1 / stepX2
    stepZ2Inv = 1 / stepZ2
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            ij = to(i, j)
            if isHole(i, j) or isBorder(i, j):
                matrA[ij][ij] = 1
                continue

            matrA[ij][ij] = -2 * (stepX2Inv + stepZ2Inv)
            matrA[ij][to(i + 1, j)] = stepX2Inv
            matrA[ij][to(i - 1, j)] = stepX2Inv
            matrA[ij][to(i, j + 1)] = stepZ2Inv
            matrA[ij][to(i, j - 1)] = stepZ2Inv
    return matrA


def main():
    random.seed()

    matrA = getMatrixA()


if __name__ == '__main__':
    main()