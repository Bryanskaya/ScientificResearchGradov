import math
import numpy as np

from simpleJacobi.Jacobi import Jacobi
from configParams import *


def f(x, z):
    return f0 * math.exp(-beta * ((x - x0) ** 2 + (z - z0) ** 2)) / k


def to(i, j=0):
    """ Transform real coordinates to matrix's A coordinates """
    return n * i + j


def toOrig(matr):
    u = np.zeros((m, n))

    for i in range(m):
        for j in range(n):
            u[i][j] = None if isHole(i, j) else matr[to(i, j)]
    return u


def isHole(i, j):
    if holeI < i < holeI + holeM and \
            holeJ < j < holeJ + holeN:
        return True
    return False


def isBorder(i, j):
    if i < holeI or i > holeI + holeM or \
            j < holeJ or j > holeJ + holeN:
        return False

    if holeI == i or i == holeI + holeM or \
            holeJ == j or j == holeJ + holeN:
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


def getVectB():
    vectB = np.zeros(n * m)

    for i in range(m):
        vectB[to(i)] = u0Left  # left
        vectB[to(i, n - 1)] = u0Right  # right
    for i in range(n):
        vectB[to(0, i)] = u0Top  # top
        vectB[to(m - 1, i)] = u0Bottom  # bottom

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if isHole(i, j):
                value = holeU0
            elif isBorder(i, j):
                value = borderTemperature(i, j)
            else:
                value = -f(j * stepX, i * stepZ)

            vectB[to(i, j)] = value
    return vectB


def simpleJacobi():
    matrA = getMatrixA()
    vectB = getVectB()
    vectX = [0] * len(vectB)

    return Jacobi(matrA, vectB, vectX)