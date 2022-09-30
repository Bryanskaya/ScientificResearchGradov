from Jacobi import Jacobi
from entity.Model import Model
import numpy as np
import matplotlib.pyplot as plt

a, b = 20, 20                   # длина, ширина
u0Left, u0Right = 200, 350      # -73, 76
u0Top, u0Bottom = 320, 320      # 47, 47
k = 10                          # теплопроводность
f0, beta = 30, 0
x0, z0 = a / 2, b / 2
n, m = 20, 20


def getInitData():
    model = Model()
    # model.setA(a)
    # model.setB(b)
    # model.setK(k)
    # model.setBeta(beta)
    # model.setF0(f0)
    # model.setX0Z0(x0, z0)
    return model


def main():
    model = getInitData()
    a = model.getMatrixA()
    b = model.getMatrixB()
    tempU = Jacobi(a, b)
    u = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            u[i][j] = tempU[m * i + j]
    print(u)

    plt.imshow(u, cmap='hot')
    plt.show()

if __name__ == '__main__':
    main()