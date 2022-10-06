from Jacobi import Jacobi
from configParams import *

import math
import numpy as np

from visualizer import draw2D, draw3D


def f(x, z):
    return f0 * math.exp(-beta * ((x - x0) ** 2 + (z - z0) ** 2)) / k


def to(i, j=0):
    """ Transform real coordinates to matrix's A coordinates """
    return n * i + j


def toOrig(matr):
    u = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            u[i][j] = None if isHole(i, j) else matr[m * i + j]
    return u


def isHole(i, j):
    if holeI < i < holeI + holeN and \
            holeJ < j < holeJ + holeM:
        return True
    return False


def isBorder(i, j):
    if i < holeI or i > holeI + holeN or \
            j < holeJ or j > holeJ + holeM:
        return False

    if holeI == i or i == holeI + holeN or \
            holeJ == j or j == holeJ + holeM:
        return True
    return False


def borderTemperature(i, j):
    if i == holeI: return u0TopInside
    if i == holeI + holeN: return u0BottomInside
    if j == holeJ: return u0LeftInside
    if j == holeJ + holeM: return u0RightInside
    print("*****", i, j)


def getMatrixA():
    stepX2 = stepX ** 2
    stepZ2 = stepZ ** 2
    tempSize = n * m
    matrA = np.zeros((tempSize, tempSize))

    for i in range(n):
        matrA[to(0, i)][to(0, i)] = 1           # top
        matrA[to(i)][to(i)] = 1                 # left
        matrA[to(i, n - 1)][to(i, n - 1)] = 1   # right
        matrA[to(m - 1, i)][to(m - 1, i)] = 1   # bottom

    stepX2Inv = 1 / stepX2
    stepZ2Inv = 1 / stepZ2
    for i in range(1, n - 1):
        for j in range(1, m - 1):
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


def getVectB():
    vectB = np.zeros(n * m)

    for i in range(n):
        vectB[to(0, i)] = u0Top  # top
        vectB[to(i)] = u0Left  # left
        vectB[to(i, n - 1)] = u0Right  # right
        vectB[to(m - 1, i)] = u0Bottom  # bottom

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if isHole(i, j):
                value = holeU0
            elif isBorder(i, j):
                value = borderTemperature(i, j)
            else:
                value = -f(i * stepX, j * stepZ)

            vectB[to(i, j)] = value
    return vectB


def main():
    matrA = getMatrixA()
    vectB = getVectB()
    vectX = [0] * len(vectB)

    matrU = Jacobi(matrA, vectB, vectX)

    # draw3D(toOrig(matrU))
    draw2D(toOrig(matrU))


if __name__ == '__main__':
    main()
