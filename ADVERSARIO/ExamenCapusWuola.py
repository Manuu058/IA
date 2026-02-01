from dataclasses import dataclass
from copy import deepcopy

@dataclass 
class Jugada:
    numero:int 

    def __init__(self, n:int):
        self.numero=n

@dataclass
class tNodo:
    tablero: list          # números libres
    conjunto_max: list     # números elegidos por MAX
    conjunto_min: list     # números elegidos por MIN
    turno_max: bool        # True si juega MAX, False si juega MIN


    def __init__(self, t:list, cmax:list,cmin:list):
        self.tablero=t
        self.conjunto_max=cmax
        self.conjunto_min=cmin
        self.turno_max=True

def estado_inicial()->tNodo:
    return tNodo([1,2,3,4,5,6,7,8,9],[],[],True)


def esValida(estado: tNodo, jugada: Jugada) -> bool:
    return jugada.numero in estado.tablero

def aplicaJugada(estado: tNodo, jugada: Jugada) -> tNodo:
    nuevo = deepcopy(estado)

    if nuevo.turno_max:
        nuevo.conjunto_max.append(jugada.numero)
    else:
        nuevo.conjunto_min.append(jugada.numero)

    nuevo.tablero.remove(jugada.numero)
    nuevo.turno_max = not nuevo.turno_max

    return nuevo

def Terminal(estado: tNodo) -> bool:
    # Comprobar MAX
    n = len(estado.conjunto_max)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if estado.conjunto_max[i] + estado.conjunto_max[j] + estado.conjunto_max[k] == 15:
                    return True

    # Comprobar MIN
    n = len(estado.conjunto_min)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if estado.conjunto_min[i] + estado.conjunto_min[j] + estado.conjunto_min[k] == 15:
                    return True

    # Empate
    return len(estado.tablero) == 0

    
def Utilidad(estado: tNodo) -> int:
    n = len(estado.conjunto_max)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if estado.conjunto_max[i] + estado.conjunto_max[j] + estado.conjunto_max[k] == 15:
                    return 100

    n = len(estado.conjunto_min)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if estado.conjunto_min[i] + estado.conjunto_min[j] + estado.conjunto_min[k] == 15:
                    return -100
                

    if len(estado.tablero)==0:
        return 0

    return 0


#Forma de hacerlo con libreria mas facil
from itertools import combinations

def Terminal(estado: tNodo) -> bool:
    # Comprobar MAX
    for a, b, c in combinations(estado.conjunto_max, 3):
        if a + b + c == 15:
            return True

    # Comprobar MIN
    for a, b, c in combinations(estado.conjunto_min, 3):
        if a + b + c == 15:
            return True

    # Empate
    return len(estado.tablero) == 0


def Utilidad(estado: tNodo) -> int:
    # Gana MAX
    for a, b, c in combinations(estado.conjunto_max, 3):
        if a + b + c == 15:
            return 100

    # Gana MIN
    for a, b, c in combinations(estado.conjunto_min, 3):
        if a + b + c == 15:
            return -100

    # Empate o no terminal
    return 0