from dataclasses import dataclass
from copy import deepcopy


@dataclass
class tEstado:
    robado:int
    cinta:list
    banco:int

    def __init__(self, robado, cinta, banco):
        self.robado=robado
        self.cinta=cinta
        self.banco=banco

operadores={
    1:"CogerIzq",
    2:"CogerDer"
}

def EsValido(op:int, estado:tEstado) -> bool:
    return len(estado.cinta)>1

def AplicaOperador(op:int, estado:tEstado) -> tEstado:
    nuevo=deepcopy(estado)

    match operadores[op]:
        case "CogerIzq":
            nuevo.robado+=nuevo.cinta.pop(0)
        case "CogerDer":
            nuevo.robado+=nuevo.cinta.pop(-1)

    nuevo.banco+=nuevo.cinta.pop(-1)

    return nuevo

def TestObjetivo(estado) -> bool:
    return estado.robado>estado.banco and len(estado.cinta)==1



