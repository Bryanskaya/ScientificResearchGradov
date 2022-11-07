import matplotlib.pyplot as plt
import plotly.graph_objects as go
from matplotlib import cm
import pandas as pd
import numpy as np
from matplotlib.gridspec import GridSpec

from configParams import b, a


def draw2D(matr):
    plt.figure(figsize=(10, 7))
    axim = plt.imshow(matr, cmap=cm.coolwarm, extent=[0, a, b, 0])
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


def drawTable(headerArr, valueArr):
    plt.rcParams["figure.figsize"] = [9, 2]
    plt.rcParams["figure.autolayout"] = True
    fig, axs = plt.subplots()
    fig.patch.set_visible(False)
    axs.axis('tight')
    axs.axis('off')
    tbl = axs.table(cellText=valueArr, colLabels=headerArr, loc='center')
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(11)
    fig.tight_layout()
    plt.show()

def drawPlats(headerArr, matrArr):
    fig = plt.figure(figsize=(14, 10))

    fig.add_subplot(2, 2, 1)
    plt.title(headerArr[0])
    plt.xlabel('x')
    plt.ylabel('z')
    axim = plt.imshow(matrArr[0], cmap=cm.coolwarm, extent=[0, a, b, 0])
    # plt.colorbar(axim)

    fig.add_subplot(2, 2, 2)
    plt.title(headerArr[1])
    plt.xlabel('x')
    plt.ylabel('z')
    axim = plt.imshow(matrArr[1], cmap=cm.coolwarm, extent=[0, a, b, 0])
    # plt.colorbar(axim)

    fig.add_subplot(2, 2, 3)
    plt.title(headerArr[2])
    plt.xlabel('x')
    plt.ylabel('z')
    axim = plt.imshow(matrArr[2], cmap=cm.coolwarm, extent=[0, a, b, 0])
    # plt.colorbar(axim)

    fig.add_subplot(2, 2, 4)
    plt.title(headerArr[3])
    plt.xlabel('x')
    plt.ylabel('z')
    axim = plt.imshow(matrArr[3], cmap=cm.coolwarm, extent=[0, a, b, 0])
    # plt.colorbar(axim)


    # fig = plt.figure(constrained_layout=True)
    # gs = GridSpec(3, 2, figure=fig)
    # tbl = fig.add_subplot(gs[0, :], xticklabels=[], yticklabels=[])
    # tbl.spines["top"].set_visible(False)
    # tbl.spines["right"].set_visible(False)
    # tbl.spines["bottom"].set_visible(False)
    # tbl.spines["left"].set_visible(False)
    # tbl.table(cellText=data, colLabels=headerSet, loc='center')
    #
    # gr1 = fig.add_subplot(gs[1, 0])
    # gr2 = fig.add_subplot(gs[1, 1])
    # gr3 = fig.add_subplot(gs[2, 0])
    # gr4 = fig.add_subplot(gs[2, 1])

    plt.show()