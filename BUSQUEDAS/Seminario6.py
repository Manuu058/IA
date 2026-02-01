from dataclasses import dataclass
from copy import deepcopy

import numpy as np

@dataclass 
class tEstado:
    tablero:np.ndarray
    posA:tuple
    posB:tuple
    posC:tuple #Apuntan al la posicion del medio

    def __init__(self, t:np.ndarray, posA:tuple, posB:tuple, posC:tuple):
        self.tablero=t
        self.posA=posA
        self.posB=posB
        self.posC=posC


def estado_inicial()-> tEstado:
    tablero=np.array([[-1,0,0,3,0,0],
                      [-1,0,0,3,0,0],
                      [0,1,0,3,0,0],
                      [1,1,1,-1,2,0],
                      [0,1,0,2,2,2]
                      [0,0,0,0,0,0]])
    return tEstado(tablero, (3,1),(4,4),(1,3))

def estado_final()-> tEstado:
    tablero=np.array([[-1,0,0,0,0,0],
                      [-1,0,0,0,0,0],
                      [0,0,0,0,0,0],
                      [0,1,0,-1,0,3],
                      [1,1,1,2,0,3]
                      [0,1,2,2,2,3]])
    return tEstado(tablero, (4,1),(5,3),(4,5))

operadores={
    1:"ArribaA",
    2:"AbajoA",
    3:"DerechaA",
    4:"IzquierdaA",
    5:"ArribaB",
    6:"AbajoB",
    7:"DerechaB",
    8:"IzquierdaB",
    9:"ArribaC",
    10:"AbajoC",
    11:"DerechaC",
    12:"IzquierdaC"
}

def esValido(op:int, estado:tEstado):
    valido=False
    pA=estado.posA
    pB=estado.posB
    pC=estado.posC
    match operadores[op]:
        case "ArribaA":
            if estado.tablero[pA[0]-1,pA[1]]==0 and estado.tablero[pA[0]-2,pA[1]]==0 and  estado.tablero[pA[0]-2,pA[1]-1]==0 and estado.tablero[pA[0]-1,pA[1]+1]==0:
                valido=True
        case "AbajoA":
            if estado.tablero[pA[0]+1,pA[1]]==0 and estado.tablero[pA[0]+2,pA[1]]==0 and  estado.tablero[pA[0]+2,pA[1]+1]==0 and estado.tablero[pA[0]+1,pA[1]-1]==0:
                valido=True
                



