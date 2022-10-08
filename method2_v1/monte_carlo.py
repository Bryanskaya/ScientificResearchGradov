import random
import math

from configParams import *


def f(x, z):
    return f0 * math.exp(-beta * ((x - x0) ** 2 + (z - z0) ** 2))


def step(i, j):
    temp = random.random()
    if rangeRight[0] <= temp < rangeRight[1]: return i, j + 1
    if rangeBottom[0] <= temp < rangeBottom[1]: return i + 1, j
    if rangeLeft[0] <= temp < rangeLeft[1]: return i, j - 1
    if rangeTop[0] <= temp < rangeTop[1]: return i - 1, j


def isBorderPlate(i, j):
    return True if i == 0 or j == 0 or i == m - 1 or j == n - 1 else False


def isBorderHole(i, j):
    if i < holeI or i > holeI + holeM or \
            j < holeJ or j > holeJ + holeN:
        return False

    if holeI == i or i == holeI + holeM or \
            holeJ == j or j == holeJ + holeN:
        return True
    return False


def isBorder(i, j):
    return isBorderPlate(i, j) or isBorderHole(i, j)


def uBorder(i, j):
    if i == 0:              return u0Top
    if i == m - 1:          return u0Bottom
    if j == 0:              return u0Left
    if j == n - 1:          return u0Right

    if i == holeI:          return u0TopInside
    if i == holeI + holeM:  return u0BottomInside
    if j == holeJ:          return u0LeftInside
    if j == holeJ + holeN:  return u0RightInside


def process(iStart, jStart):
    u = 0
    for _ in range(nItems):
        a, nPoints = 0, 0
        i, j = iStart, jStart
        while not isBorder(i, j):
            a += f(j * stepX, i * stepZ)
            nPoints += 1
            i, j = step(i, j)
        u += 1 / k * a / nPoints + uBorder(i, j)
    return u / nItems


def monte_carlo(matrU):
    for i in range(m):
        for j in range(n):
            if matrU[i][j] == 0:
                matrU[i][j] = process(i, j)
    return matrU

