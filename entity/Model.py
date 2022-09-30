import math
import numpy as np


class Model:
    u0Left, u0Right, u0Top, u0Bottom = -100, 500, 400, 400
    a, b = 20, 20
    f0, beta = 30, 5
    x0, z0 = a / 2, b / 2
    k = 10
    n, m = 20, 20
    stepX, stepZ = a / n, b / m

    def setU0Left(self, u0):        self.u0Left = u0
    def setU0Right(self, u0):       self.u0Right = u0
    def setU0Top(self, u0):         self.u0Top = u0
    def setU0Bottom(self, u0):      self.u0Bottom = u0
    def setA(self, a):
        self.a = a
        self.stepX = self.a / self.n
    def setB(self, b):
        self.b = b
        self.stepZ = self.b / self.m
    def setF0(self, f0):            self.f0 = f0
    def setBeta(self, beta):
        if beta < 0:
            print('Error: beta must be positive.')
            return
        self.beta = beta

    def setX0Z0(self, x0, z0):
        self.x0 = x0
        self.z0 = z0

    def setK(self, k):              self.k = k
    def setNM(self, n, m):
        self.n = n
        self.m = m
        self.stepX = self.a / self.n
        self.stepZ = self.b / self.m

    def f(self, x, z):
        return self.f0 * math.exp(-self.beta * (x - self.x0)**2 * (z - self.z0)**2) / self.k

    def getU0Right(self): return self.u0Right
    def getU0Top(self): return self.u0Top
    def getU0Bottom(self): return self.u0Bottom


    def to(self, i, j = 0):
        """
        Transform real coordinates to matrix's A coordinates
        """
        return self.n * i + j

    def getMatrixA(self):
        stepX2 = self.stepX ** 2
        stepZ2 = self.stepZ ** 2
        tempSize = self.n * self.m
        a = np.zeros((tempSize, tempSize))

        for i in range(self.n):
            a[self.to(0, i)][self.to(0, i)] = 1 # top
            a[self.to(i)][self.to(i)] = 1 # left
            a[self.to(i, self.n - 1)][self.to(i, self.n - 1)] = 1 # right
            a[self.to(self.m - 1, i)][self.to(self.m - 1, i)] = 1 # bottom

        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                a[self.to(i, j)][self.to(i, j)] = -2 * (1 / stepX2 + 1 / stepZ2)
                a[self.to(i, j)][self.to(i + 1, j)] = 1 / stepX2
                a[self.to(i, j)][self.to(i - 1, j)] = 1 / stepX2
                a[self.to(i, j)][self.to(i, j + 1)] = 1 / stepZ2
                a[self.to(i, j)][self.to(i, j - 1)] = 1 / stepZ2
        return a

    def getMatrixB(self):
        b = np.zeros(self.n * self.m)

        for i in range(self.n):
            b[self.to(0, i)] = self.u0Top               # top
            b[self.to(i)] = self.u0Left                 # left
            b[self.to(i, self.n - 1)] = self.u0Right    # right
            b[self.to(self.m - 1, i)] = self.u0Bottom   # bottom

        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                b[self.to(i, j)] = self.f(i * self.stepX, j * self.stepZ)
        return b
