from dataclasses import dataclass
from copy import deepcopy
import numpy as np

@dataclass
class tEstado:
    N:int
    fila:int
    columna:int

    def __init__(self, N:int, f:int, c:int):
        self.N=N
        self.fila=f
        self.columna=c


obstaculos=[
    (1,2), (1,7), (1,8)
]

def Amenaza(fila:int, columna:int) -> bool:

    if(fila,columna) in obstaculos:
        return True
    
    #Torre
    if fila==1 or columna==7: 
        return True
    
    #Reina (diagonales)
    if abs(fila - 1) == abs(columna - 2):
        return True

    #Rey
    if abs(fila - 1) <= 1 and abs(columna - 8) <= 1:
        return True

operaciones=[
    (2,1),
    (2,-1),
    (-2,1),
    (-2,-1),
    (1,2),
    (1,-2),
    (-1,2),
    (-1,-2)
]

def estado_inicial() -> tEstado:
    return tEstado(8,3,5)

def estado_final() -> tEstado:
    return tEstado(8,4,8)

def esValida(op:int,estado:tEstado)-> bool:
    f=estado.fila
    c=estado.columna
    valido=True
    match operaciones[op]:
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

    if Amenaza(f,c):
        valido= False
    if f>estado.N or f<1:
        valido=False
    if c>estado.N or c<1:
        valido=False
    
    return valido


def AplicaOperador(op:int, estado:tEstado)-> tEstado: 
    nuevo=deepcopy(estado)
    match operaciones[op]:
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
            nuevo.fila-=2

    return nuevo

def TestObjetivo(estado:tEstado) -> tEstado:
    return estado.fila==estado_final().fila and estado.columna==estado_final().columna


def Heuristica(estado:tEstado)-> int:
    return ((estado.fila-estado_final().fila)+(estado.columna-estado_final().columna))/3

