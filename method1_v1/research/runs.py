from parallelJacobi import processParallelJacobi
from parallelMonteCarlo import processParallelMonteCarlo
from simpleJacobi import processSimpleJacobi
from simpleMonteCarlo import processSimpleMonteCarlo


def _runSimpleJacobi():
    matrU = processSimpleJacobi.simpleJacobi()
    return processSimpleJacobi.toOrig(matrU)


def _runParallelJacobi():
    matrU = processParallelJacobi.parallelJacobi()
    return processParallelJacobi.toOrig(matrU)


def _runSimpleMonteCarlo():
    return processSimpleMonteCarlo.simpleMonteCarlo()


def _runParallelMonteCarlo():
    return processParallelMonteCarlo.parallelMonteCarlo()
