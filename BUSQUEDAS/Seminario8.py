from dataclasses import dataclass
from copy import deepcopy

import numpy as np

@dataclass
class tEstado:
    N:int
    fila:int 
    columna:int
    tablero:np.ndarray


operadores={
    1:"ArribaIzq",
    2:"ArribaDer",
    3:"AbajoIzq",
    4:"AbajoDer"
}

obstaculo=[
    (0,4),
    (1,2),
    (2,2),
    (4,4),
    (2,3),
    (3,4),
    (2,5),
    (1,6)
]

def estado_inicial() -> tEstado:
    return tEstado(7,0,0)

def estado_final() -> tEstado:
    return tEstado(7,2,6)

def testObjetivo(estado:tEstado) ->bool:
    return estado.fila==estado_final().fila and estado_final().columna==estado.columna

def esValido(estado:tEstado,op:int) -> bool:
    valido=True
    f=estado.fila
    c=estado.columna

    match operadores[op]:
        case "ArribaIzq":
            f=f-1
            c=c-1
        case "ArribaDer":
            f=f-1
            c=c+1
        case "AbajoIzq":
            f=f+1
            c=c-1
        case "AbajoDer":
            f=f+1
            c=c+1


    if (f,c) in obstaculo:
        valido=False
    if(f<0 or f>=estado.N):
        valido=False
    if(c<0 or c>=estado.N):
        valido=False
    
    return valido

def aplicaOperador(estado:tEstado,op:int) -> tEstado:
    nuevo=deepcopy(estado)

    match operadores[op]:
        case "ArribaIzq":
            nuevo.fila=nuevo.fila-1
            nuevo.columna=nuevo.columna-1
        case "ArribaDer":
            nuevo.fila=nuevo.fila-1
            nuevo.columna=nuevo.columna+1
        case "AbajoIzq":
            nuevo.fila=nuevo.fila+1
            nuevo.columna=nuevo.columna-1
        case "AbajoDer":
            nuevo.fila=nuevo.fila+1
            nuevo.columna=nuevo.columna+1
    
    return nuevo


def heuristica(estado:tEstado) -> int:
    return max(abs(estado.fila-estado_final().fila),abs(estado.columna-estado_final().columna))


