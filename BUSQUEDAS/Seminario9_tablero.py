from dataclasses import dataclass 
from copy import deepcopy

import numpy as np 

@dataclass
class tEstado:
    tablero:np.ndarray
    fila:int 
    columna:int 
    N:int

    def __init__(self, t:np.ndarray, f:int, c:int, N:int):
        self.tablero=t
        self.fila=f
        self.columna=c
        self.N=N


def estado_inicial()->tEstado:
    tablero=np.array([[1,1,1,1,1,1,1,1],
                      [1,1,1,0,0,0,1,1],
                      [0,1,0,1,2,0,1,0],
                      [0,1,0,0,1,0,1,0],
                      [0,1,0,0,0,1,1,0],
                      [0,1,0,0,0,0,1,0],
                      [0,1,0,0,0,0,1,1],
                      [0,1,0,0,0,0,1,0]])
    return tEstado(tablero, 2,4,8)

def estado_final()->tEstado:
    tablero=np.array([[1,1,1,1,1,1,1,1],
                     [1,1,1,0,0,0,1,1],
                     [0,1,0,1,0,0,1,0],
                     [0,1,0,0,1,0,1,2],
                     [0,1,0,0,0,1,1,0],
                     [0,1,0,0,0,0,1,0],
                     [0,1,0,0,0,0,1,1],
                     [0,1,0,0,0,0,1,0]])
    return tEstado(tablero, 3,7,8)


operadores=[
    (2,1),
    (2,-1),
    (-2,1),
    (-2,-1),
    (1,2),
    (1,-2),
    (-1,2),
    (-1,-2)
]

def esValido(op:int, estado:tEstado)->bool:
    valido=True
    f=estado.fila
    c=estado.columna
    match operadores[op]:
        case (2,1):
            f+=2
            c+=1
        case (2,-1):
            f+=2
            c-=1
        case (-2,1):
            f-=2
            c+=1
        case (-2,-1):
            f-=2
            c-=1
        case (1,2):
            f+=1
            c+=2
        case (1,-2):
            f+=1
            c-=2
        case (-1,2):
            f-=1
            c+=2
        case (-1,-2):
            f-=1
            c-=2

    if f>estado.N-1 or f<0:
        valido=False
    if c>estado.N-1 or c<0:
        valido=False
    
    if estado.tablero[f,c]==1:
        valido=False

    
    return valido

def aplicaOperador(op:int, estado:tEstado)->tEstado:
    nuevo=deepcopy(estado)
    f=nuevo.fila
    c=nuevo.columna
    match operadores[op]:
        case (2,1):
            nuevo.fila+=2
            nuevo.columna+=1
        case (2,-1):
            nuevo.fila+=2
            nuevo.columna-=1
        case (-2,1):
            nuevo.fila-=2
            nuevo.columna+=1
        case (-2,-1):
            nuevo.fila-=2
            nuevo.columna-=1
        case (1,2):
            nuevo.fila+=1
            nuevo.columna+=2
        case (1,-2):
            nuevo.fila+=1
            nuevo.columna-=2
        case (-1,2):
            nuevo.fila-=1
            nuevo.columna+=2
        case (-1,-2):
            nuevo.fila-=1
            nuevo.columna-=2

    nuevo.tablero[nuevo.fila,nuevo.columna]=2
    nuevo.tablero[f,c]=0

    return nuevo

def TestObjetivo(estado:tEstado)->bool:
    if estado.tablero==estado_final().tablero:
        return True
    
    return False





