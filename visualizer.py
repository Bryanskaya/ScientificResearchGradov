import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def draw2D(matr):
    plt.imshow(matr, cmap=cm.coolwarm)
    # plt.imshow(matr, cmap='hot')
    plt.show()


def draw3D(matr):
    # (fig, ax, surf) = surface_plot(matr, cmap=plt.cm.coolwarm)

    (x, y) = np.meshgrid(np.arange(matr.shape[0]), np.arange(matr.shape[1]))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(x, y, matr, cmap='hot')

    fig.colorbar(surf)

    ax.set_xlabel('X')
    ax.set_ylabel('Z')
    ax.set_zlabel('U')

    plt.show()


# def surface_plot (matr, **kwargs):
#     (x, y) = np.meshgrid(np.arange(matr.shape[0]), np.arange(matr.shape[1]))
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     surf = ax.plot_surface(x, y, matr, **kwargs)
#     return (fig, ax, surf)


