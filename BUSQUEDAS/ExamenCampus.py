from dataclasses import dataclass 
from copy import deepcopy


@dataclass
class tEstado:
    piloto:str
    copiloto:str
    centro_izqcentro:str
    centro_der:str
    atras_der:str
    atras_izq:str

    def __init__(self, p:str,c:str,ci:str,cd:str,ad:str,ai:str):
        self.piloto=p
        self.copiloto=c
        self.centro_izqcentro=ci
        self.centro_der=cd
        self.atras_der=ad
        self.atras_izq=ai

    
def estado_inicial()-> tEstado:
    return tEstado("desplazados","desplazados","normal","normal","abatidos","abatidos")

def estado_final()->tEstado:
    return tEstado("normal","normal","abatidos","abatidos","normal","normal")

operadores={
    1:"desplazarpiloto",
    2:"desplazarcopiloto",
    3:"abatircentro_doble",
    4:"desabatircentro_doble",
    5:"abatircentro_derecha",
    6:"desabatircentro_derecha",
    7:"abatiratras_derecha",
    8:"desabatiratras_derecha",
    9:"abatiratras_izquierda",
    10:"desabatiratras_izquierda"
}

def esValida(op: int, estado: tEstado) -> bool:

    match operadores[op]:

        # PILOTO
        case "desplazarpiloto":
            return (
                estado.piloto == "normal" and
                estado.centro_izqcentro == "normal"
            )

        # COPILOTO
        case "desplazarcopiloto":
            return (
                estado.copiloto == "normal" and
                estado.centro_der == "normal"
            )

        # SEGUNDA FILA (DOBLE)
        case "abatircentro_doble":
            return (
                estado.centro_izqcentro == "normal" and
                estado.piloto == "normal"
            )

        case "desabatircentro_doble":
            return estado.centro_izqcentro == "abatidos"

        # SEGUNDA FILA (DERECHA)
        case "abatircentro_derecha":
            return (
                estado.centro_der == "normal" and
                estado.copiloto == "normal"
            )

        case "desabatircentro_derecha":
            return estado.centro_der == "abatidos"

        # TERCERA FILA
        case "abatiratras_derecha":
            return estado.atras_der == "normal"

        case "desabatiratras_derecha":
            return estado.atras_der == "abatidos"

        case "abatiratras_izquierda":
            return estado.atras_izq == "normal"

        case "desabatiratras_izquierda":
            return estado.atras_izq == "abatidos"

    return False

def AplicaOperador(op:int, estado:tEstado)->tEstado:
    nuevo=deepcopy(estado)

    match operadores[op]:
        # PILOTO
        case "desplazarpiloto":
            if(nuevo.piloto =="desplazados"):
                nuevo.piloto="normal"
            else:
                nuevo.piloto="desplazados"

        # COPILOTO
        case "desplazarcopiloto":
            if(nuevo.copiloto =="desplazados"):
                nuevo.copiloto="normal"
            else:
                nuevo.copiloto="desplazados"

        # SEGUNDA FILA (DOBLE)
        case "abatircentro_doble":
            nuevo.centro_izqcentro="abatidos"

        case "desabatircentro_doble":
            nuevo.centro_izqcentro="normal"
        # SEGUNDA FILA (DERECHA)
        case "abatircentro_derecha":
           nuevo.centro_der="abatidos"

        case "desabatircentro_derecha":
            nuevo.centro_der="normal"

        # TERCERA FILA
        case "abatiratras_derecha":
           nuevo.atras_der="abatidos"

        case "desabatiratras_derecha":
            nuevo.atras_der="normal"

        case "abatiratras_izquierda":
           nuevo.atras_izq="abatidos"

        case "desabatiratras_izquierda":
            nuevo.atras_izq="normal"

    return nuevo

def testObjetivo(estado:tEstado)->bool:
    return (estado_final().piloto==estado.piloto and estado_final().copiloto==estado.copiloto and
            estado_final().centro_izqcentro==estado.centro_izqcentro and estado_final().centro_der==estado.centro_der and 
            estado_final().atras_der==estado.atras_der and estado_final().atras_izq==estado.atras_izq)



def heuristica(estado:tEstado)-> int:
    h=0
    objetivo=estado_final()

    if(estado.piloto != objetivo.piloto):
        h+=1
    if(estado.copiloto != objetivo.copiloto):
        h+=1
    if(estado.centro_izqcentro != objetivo.centro_izqcentro):
        h=h+1
    if(estado.centro_der != objetivo.centro_der):
        h=h+1
    if(estado.atras_der != objetivo.atras_der):
        h=h+1
    if(estado.atras_izq != objetivo.atras_izq):
        h=h+1

    return h

##Es admisible porque no sobreestima el coste real de alcanzar el objetivo 