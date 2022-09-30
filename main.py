from Jacobi import Jacobi
from configParams import *

import math
import numpy as np

from visualizer import draw2D, draw3D


def f(x, z):
    return f0 * math.exp(beta * (x - x0) ** 2 * (z - z0) ** 2) / k


def to(i, j=0):
    """ Transform real coordinates to matrix's A coordinates """
    return n * i + j


def toOrig(matr):
    u = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            u[i][j] = matr[m * i + j]
    return u


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
            matrA[ij][ij] = -2 * (stepX2Inv + stepZ2Inv)
            matrA[ij][to(i + 1, j)] = stepX2Inv
            matrA[ij][to(i - 1, j)] = stepX2Inv
            matrA[ij][to(i, j + 1)] = stepZ2Inv
            matrA[ij][to(i, j - 1)] = stepZ2Inv
    return matrA


def getMatrixB():
    matrB = np.zeros(n * m)

    for i in range(n):
        matrB[to(0, i)] = u0Top                 # top
        matrB[to(i)] = u0Left                   # left
        matrB[to(i, n - 1)] = u0Right           # right
        matrB[to(m - 1, i)] = u0Bottom          # bottom

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            matrB[to(i, j)] = f(i * stepX, j * stepZ)
    return matrB


def main():
    matrA = getMatrixA()
    matrB = getMatrixB()

    matrU = Jacobi(matrA, matrB)

    draw3D(toOrig(matrU))


if __name__ == '__main__':
    main()
