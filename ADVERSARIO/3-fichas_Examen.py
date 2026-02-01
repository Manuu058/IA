from dataclasses import dataclass
from copy import deepcopy

import numpy as np 

@dataclass
class tNodo:
    tablero:np.ndarray
    N:int

    
    def __init__(self, N:int,tablero:np.ndarray):
        self.N=N
        self.tablero=tablero


@dataclass
class tJugada:
    ficha:tuple
    movimiento:tuple
    




def estado_inicial() -> tNodo:
    tablero = np.array([
        [ 1,  1,  1],
        [ 0,  0,  0],
        [-1, -1, -1]
    ])
    return tNodo(3, tablero)



def esValida(jugada: tJugada, nodo: tNodo) -> bool:
    valido=True
    a, b = jugada.ficha
    df, dc = jugada.movimiento

    nf = a + df
    nc = b + dc

    # Límites del tablero
    if nf < 0 or nf >= nodo.N or nc < 0 or nc >= nodo.N:
       valido=False
    
    if dc==0 and nodo.tablero[nf,nc]!=0:
        valido=False
    if dc==1 and nodo.tablero[nf,nc]!=-1:
        valido=False
    if dc==-1 and nodo.tablero[nf,nc]!=-1:
        valido=False
    return valido

    


def AplicaOperador(jugada:tJugada, nodo:tNodo) -> tNodo:
    nuevo=deepcopy(nodo)

    (a,b)=jugada.ficha
    match jugada.movimiento:
        case (1,0):
           nuevo.tablero[a+1,b]=1
        case (1,1):
            nuevo.tablero[a+1,b+1]=1
        case (1,-1):
            nuevo.tablero[a+1,b-1]=1

    nuevo.tablero[a,b]=0
    
    return nuevo

def Terminal(nodo: tNodo) -> bool:
    termina = False

    for i in range(nodo.N):
        if nodo.tablero[0, i] == -1:
            termina = True
        if nodo.tablero[nodo.N - 1, i] == 1:
            termina = True

    if not np.any(nodo.tablero == 1): ##El any devuelve si existe en el tablero algun elemento =1
        termina = True
    if not np.any(nodo.tablero == -1):
        termina = True

    return termina


def Utilidad(nodo: tNodo) -> int:

    for i in range(nodo.N):
        if nodo.tablero[0, i] == -1:
            valor=-100
        if nodo.tablero[nodo.N - 1, i] == 1:
            valor=100

    if not np.any(nodo.tablero == 1): ##El any devuelve si existe en el tablero algun elemento =1
        valor=-100
    if not np.any(nodo.tablero == -1):
        valor=100
    return valor

        
        
            
    
    
    


    

