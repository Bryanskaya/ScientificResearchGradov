from research.research import runTimeSize
from research.runs import _runParallelJacobi, _runSimpleMonteCarlo, _runParallelMonteCarlo, _runSimpleJacobi
from visualizer import draw2D, drawTable, drawPlats
from configParams import *

import time
import random


def runSimpleJacobi():
    matrU = _runSimpleJacobi()
    draw2D(matrU)


def runParallelJacobi():
    matrU = _runParallelJacobi()
    draw2D(matrU)


def runSimpleMonteCarlo():
    matrU = _runSimpleMonteCarlo()
    draw2D(matrU)


def runParallelMonteCarlo():
    matrU = _runParallelMonteCarlo()
    draw2D(matrU)


def runTime():
    headerArr = ["Название", "Время"]
    methodArr = ['Метод Якоби', 'Метод Якоби (с распараллеливанием)',
                 'Метод Монте-Карло', 'Метод Монте-Карло (с распараллеливанием)']
    funcArr = [_runSimpleJacobi,
               _runParallelJacobi,
               _runSimpleMonteCarlo,
               _runParallelMonteCarlo]

    matrUArr = [0] * len(funcArr)
    timeArr = []
    for i in range(len(funcArr)):
        start = time.time()
        matrUArr[i] = funcArr[i]()
        timeArr.append([methodArr[i], time.time() - start])

    # drawTable(headerArr, np.array(timeArr))
    drawPlats(methodArr, matrUArr)


def main():
    random.seed()

    # runSimpleJacobi()
    # runParallelJacobi()
    # runSimpleMonteCarlo()
    # runParallelMonteCarlo()
    # runTime()

    runTimeSize()


if __name__ == '__main__':
    main()
