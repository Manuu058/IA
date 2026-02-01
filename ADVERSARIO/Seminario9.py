from dataclasses import dataclass
from copy import deepcopy 

@dataclass
class Jugada:
    palo:str
    numero:int

@dataclass
class Estado:
    mesa: dict          # {"Oro": [min, max], "Basto": [min, max]}
    mano_max: dict      # {"Oro": [...], "Basto": [...]}
    mano_min: dict
    turno: int          # 1 = MAX, -1 = MIN


def es_valida(estado: Estado, jugada: Jugada) -> bool:
    if estado.turno == 1:
        mano = estado.mano_max
    else: 
        mano =estado.mano_min

    # ¿Tiene la carta?
    if jugada.numero not in mano[jugada.palo]:
        return False

    minimo, maximo = estado.mesa[jugada.palo]

    # ¿Encaja en la mesa?
    return jugada.numero == minimo - 1 or jugada.numero == maximo + 1



def aplicar_jugada(estado: Estado, jugada: Jugada) -> Estado:
    nuevo = deepcopy(estado)
    if estado.turno == 1:
        mano = estado.mano_max
    else: 
        mano =estado.mano_min

    # Quitar carta de la mano
    mano[jugada.palo].remove(jugada.numero)

    # Actualizar mesa
    minimo, maximo = nuevo.mesa[jugada.palo]
    if jugada.numero < minimo:
        nuevo.mesa[jugada.palo][0] = jugada.numero
    else:
        nuevo.mesa[jugada.palo][1] = jugada.numero

    # Cambiar turno
    nuevo.turno *= -1

    return nuevo


def es_terminal(estado: Estado) -> bool:
    return (
        len(estado.mano_max["Oro"]) + len(estado.mano_max["Basto"]) == 0 or
        len(estado.mano_min["Oro"]) + len(estado.mano_min["Basto"]) == 0
    )

def utilidad(estado: Estado) -> int:
    if not es_terminal(estado):
        return 0

    if len(estado.mano_max["Oro"]) + len(estado.mano_max["Basto"]) == 0:
        return 1     # gana MAX
    else:
        return -1    # gana MIN



