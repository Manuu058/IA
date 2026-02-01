from dataclasses import dataclass
from copy import deepcopy

import numpy as np

@dataclass
class tEstado:
    tablero:np.ndarray
    filas:int 
    columnas:int
    filaobjeto:list
    columnaobjeto:list


    def __init__(self, tablero, filas, columnas, filaobjeto, columnaobjeto):
        self.tablero=tablero
        self.filas=filas
        self.columnas=columnas
        self.filaobjeto=filaobjeto
        self.columnaobjeto=columnaobjeto

operadores={
    1: "ArribaA",
    2: "AbajoA",
    3: "DrchaA",
    4: "IzqdaA",
    5: "ArribaB",
    6: "AbajoB",
    7: "DrchaB",
    8: "IzqdaB",
    9: "ArribaC",
    10: "AbajoC",
    11: "DrchaC",
    12: "IzqdaC"
}

def EstadoInicial() -> tEstado:
    return tEstado(np.array([[-1,0,0,3,0,0],
                             [-1,0,0,3,0,0],
                             [0,1,0,3,0,0],
                             [1,1,1,-1,2,0],
                             [0,1,0,2,2,2],
                             [0,0,0,0,0,0]]),
                   [3,1,4],
                   [1,3,4])

def estadoFinal() -> tEstado:
    return tEstado(np.array([[-1,0,0,0,0,0],
                             [-1,0,0,0,0,0],
                             [0,0,0,0,0,0],
                             [0,1,0,-1,0,3],
                             [1,1,1,2,0,3],
                             [0,1,2,2,2,3]]),
                   [4,5,4],
                   [1,3,5])

def EsValido()