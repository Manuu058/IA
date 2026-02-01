from dataclasses import dataclass
from copy import deepcopy

import numpy as np 

@dataclass
class tEstado:
    filaRobot:int
    columnaRobot:int
    filaRaton:int
    columnaRaton:int 
    N:int
    tablero:np.ndarray

    def __init__(self, fRobot:int, cRobot:int, fRaton:int, cRaton:int, N:int):
        self.filaRobot=fRobot
        self.columnaRobot=cRobot
        self.filaRaton=fRaton
        self.columnaRaton=cRaton
        self.N=N

    
def estado_inicial()->tEstado:
    return tEstado(7,3,3,3,7)

obstaculos=[
    (2,2),(3,2),(4,4),(6,1),(6,3),(6,6),(7,1),(7,2),(7,6)
]

operaciones_Robot={
    1: "Arriba",
    2: "Abajo",
    3: "Derecha",
    4: "Izquierda"
}

def esValido(op:int, estado:tEstado) ->bool:
    valida=True

    f=estado.filaRobot
    c=estado.columnaRobot

    a=estado.filaRaton
    b=estado.columnaRaton

    match operaciones_Robot[op]:
        case "Arriba":
            f-=1
        case "Abajo":
            f+=1
        case "Derecha":
            c+=1
        case "Izquierda":
            c-=1
    
    match operaciones_Robot[op]:
        case "Arriba" | "Abajo":
            if (a, b) != (1, 1):
                a -= 1
                b -= 1
        case "Derecha" | "Izquierda":
            if (a, b) != (estado.N, estado.N):
                a += 1
                b += 1
    if f == a and c == b:
        valida = False

    
    if (f,c) in obstaculos:
        valida=False

    if( f>estado.N or f<1):
        valida=False

    if(c>estado.N or c<1):
        valida=False
    
    return valida

def aplicaOperador(op:int, estado:tEstado) ->tEstado:
    nuevo=deepcopy(estado)
        
    match operaciones_Robot[op]:
        case "Arriba":
            nuevo.filaRaton-=1
            nuevo.columnaRaton-=1
            nuevo.filaRobot-=1
        case "Abajo":
            nuevo.filaRaton-=1
            nuevo.columnaRaton-=1
            nuevo.filaRobot+=1
        case "Derecha":
            nuevo.filaRaton+=1
            nuevo.columnaRaton+=1
            nuevo.columnaRobot+=1
        case "Izquierda":
            nuevo.filaRaton+=1
            nuevo.columnaRaton+=1
            nuevo.columnaRobot-=1

    return nuevo

def testObjetivo(estado:tEstado) ->bool:
    if estado.filaRobot ==estado.N and estado.columnaRobot==estado.N:
        return True
    
    return False
