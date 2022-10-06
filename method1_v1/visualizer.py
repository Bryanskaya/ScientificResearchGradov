import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

from configParams import b, a


def draw2D(matr):
    axim = plt.imshow(matr, cmap=cm.coolwarm, extent=[0, b, a, 0])
    plt.colorbar(axim)
    plt.xlabel('x')
    plt.ylabel('z')
    # plt.imshow(matr, cmap='hot')
    plt.show()


def draw3D(matr):
    # (fig, ax, surf) = surface_plot(matr, cmap=plt.cm.coolwarm)

    (x, y) = np.meshgrid(np.arange(matr.shape[0]), np.arange(matr.shape[1]))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(x, y, matr, cmap=cm.coolwarm)

    fig.colorbar(surf)

    ax.set_xlabel('X')
    ax.set_ylabel('Z')
    ax.set_zlabel('U')

    plt.show()