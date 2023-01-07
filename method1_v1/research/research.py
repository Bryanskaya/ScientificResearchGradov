import time

from configParams import *
from ioData.writer import loadData, writeData
from parallelMonteCarlo.MonteCarlo import monte_carlo, process
from parallelMonteCarlo.processParallelMonteCarlo import getMatrix
from research.runs import _runSimpleJacobi, _runParallelJacobi, _runSimpleMonteCarlo, _runParallelMonteCarlo
from visualizer import draw2D


def runTimeSize():
    # methodDict = {'Jacobi': _runSimpleJacobi,
    #               'Jacobi-parallel': _runParallelJacobi,
    #               'Monte-Carlo': _runSimpleMonteCarlo,
    #               'Monte-Carlo-parallel': _runParallelMonteCarlo}

    methodDict = {'Jacobi-parallel': _runParallelJacobi}

    data = loadData()
    if not data:
        for name in methodDict:
            data[name] = {}

    for name, f in methodDict.items():
        if name not in methodDict:
            data[name] = {}

        start = time.time()
        f()
        data[name][n * m] = time.time() - start

        #writeData(data)
        print(name, n*m, data[name][n * m])


def runOnePoint():
    matrA = getMatrix()
    start = time.time()
    process(round(7.5 / stepZ), round(2.7 / stepX), matrA)
    print(time.time() - start)
