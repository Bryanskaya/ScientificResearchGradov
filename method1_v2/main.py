from Jacobi import Jacobi
from configParams import *
from numba import njit, prange, types
from numba.typed import List, Dict

import math
import numpy as np

from visualizer import draw2D, draw3D


@njit
def f(x, z):
    return f0 * math.exp(-beta * ((x - x0) ** 2 + (z - z0) ** 2)) / k


@njit
def to(i, j=0):
    """ Transform real coordinates to matrix's A coordinates """
    return n * i + j


def toOrig(matr):
    u = np.zeros((m, n))

    for i in range(m):
        for j in range(n):
            u[i][j] = None if isHole(i, j) else matr[to(i, j)]
    return u


@njit
def isHole(i, j):
    if holeI < i < holeI + holeM and \
            holeJ < j < holeJ + holeN:
        return True
    return False


@njit
def isBorder(i, j):
    if i < holeI or i > holeI + holeM or \
            j < holeJ or j > holeJ + holeN:
        return False

    if holeI == i or i == holeI + holeM or \
            holeJ == j or j == holeJ + holeN:
        return True
    return False


@njit
def borderTemperature(i, j):
    if i == holeI: return u0TopInside
    if i == holeI + holeM: return u0BottomInside
    if j == holeJ: return u0LeftInside
    if j == holeJ + holeN: return u0RightInside
    print("*****", i, j)


@njit(parallel=True)
def getMatrixA():
    stepX2 = stepX ** 2
    stepZ2 = stepZ ** 2
    tempSize = n * m
    # matrA = np.zeros((tempSize, tempSize))
    matrA = List()
    for _ in range(tempSize):
        matrA.append(Dict.empty(key_type=types.int64, value_type=types.float64))

    for i in prange(m):
        matrA[to(i)][to(i)] = 1                 # left
        matrA[to(i, n - 1)][to(i, n - 1)] = 1   # right
    for i in prange(n):
        matrA[to(0, i)][to(0, i)] = 1           # top
        matrA[to(m - 1, i)][to(m - 1, i)] = 1   # bottom

    stepX2Inv = 1 / stepX2
    stepZ2Inv = 1 / stepZ2
    for i in prange(1, m - 1):
        for j in prange(1, n - 1):
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


@njit(parallel=True)
def getVectB():
    vectB = np.zeros(n * m)

    for i in prange(m):
        vectB[to(i)] = u0Left  # left
        vectB[to(i, n - 1)] = u0Right  # right
    for i in prange(n):
        vectB[to(0, i)] = u0Top  # top
        vectB[to(m - 1, i)] = u0Bottom  # bottom

    for i in prange(1, m - 1):
        for j in prange(1, n - 1):
            if isHole(i, j):
                value = holeU0
            elif isBorder(i, j):
                value = borderTemperature(i, j)
            else:
                value = -f(j * stepX, i * stepZ)

            vectB[to(i, j)] = value
    return vectB


def main():
    matrA = getMatrixA()
    vectB = getVectB()

    matrU = Jacobi(matrA, vectB)

    # draw3D(toOrig(matrU))
    draw2D(toOrig(matrU))


if __name__ == '__main__':
    main()
