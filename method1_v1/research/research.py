import time

from configParams import *
from ioData.writer import loadData, writeData
from research.runs import _runSimpleJacobi, _runParallelJacobi, _runSimpleMonteCarlo, _runParallelMonteCarlo


def runTimeSize():
    methodDict = {'Jacobi': _runSimpleJacobi,
                  'Jacobi-parallel': _runParallelJacobi,
                  'Monte-Carlo': _runSimpleMonteCarlo,
                  'Monte-Carlo-parallel': _runParallelMonteCarlo}

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

        writeData(data)
        print(name)
