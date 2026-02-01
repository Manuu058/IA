from dataclasses import dataclass 
from copy import deepcopy

@dataclass

class tEstado:
    misionerosizq:int
    canivalesizq:int
    misionerosder:int
    canivalesder:int
    barcaizq:bool

    def __init__(self, mizq,cizq,mder,cder):
        self.misionerosizq=mizq
        self.canivalesizq=cizq
        self.misionerosder=mder
        self.canivalesder=cder
        self.barcaizq=True


operadores={
    1:"Mover1canibal",
    2:"Mover2canibal",
    3:"Mover1canibal1misionero",
    4:"Mover1misionero",
    5:"Mover2misionero"
}

def estado_inicial() -> tEstado:
    return tEstado(3,3,0,0)

def estado_final() -> tEstado:
    return tEstado(0,0,3,3)

def testObjetivo(estado:tEstado) -> bool:
    return  estado.canivalesizq==0 and estado.misionerosizq==0

def esValido(op:int, estado:tEstado) -> bool:
    valido=False

    match operadores[op]:
        case "Mover1canibal":
            if(estado.barcaizq):
                if(estado.canivalesizq>=1 and estado.canivalesizq-1 <= estado.misionerosizq and estado.canivalesder+1<=estado.misionerosder):
                    valido=True
            else:
                if(estado.canivalesder>=1 and estado.canivalesder-1 <= estado.misionerosder and estado.canivalesizq+1 <= estado.misionerosizq):
                    valido=True
        case "Mover2canibal":
            if(estado.barcaizq):
                if(estado.barcaizq):
                    if(estado.canivalesizq>=2 and estado.canivalesizq-2 <= estado.misionerosizq and estado.canivalesder+2<=estado.misionerosder):
                        valido=True
            else:
                if(estado.canivalesder>=2 and estado.canivalesder-2 <= estado.misionerosder and estado.canivalesizq+2 <= estado.misionerosizq):
                    valido=True
        case "Mover1canibal1misionero":
            valido=True
        case "Mover1misionero":
            if(estado.barcaizq):
                if(estado.misionerosizq>=1 and estado.canivalesizq <= estado.misionerosizq-1 and estado.canivalesder<=estado.misionerosder+1):
                    valido=True
            else:
                    if(estado.canivalesder>=1 and estado.canivalesder <= estado.misionerosder-1 and estado.canivalesizq <= estado.misionerosizq+1):
                     valido=True
        case "Mover2misionero":
            if(estado.barcaizq):
                if(estado.misionerosizq>=2 and estado.canivalesizq <= estado.misionerosizq-2 and estado.canivalesder<=estado.misionerosder+2):
                    valido=True
            else:
                    if(estado.canivalesder>=2 and estado.canivalesder <= estado.misionerosder-2 and estado.canivalesizq <= estado.misionerosizq+2):
                        valido=True
    
    return valido

def AplicaOperador(op:int, estado:tEstado) -> tEstado:
    nuevo=deepcopy(estado)

    match operadores[op]:
        case "Mover1canibal":
            if(estado.barcaizq):
                nuevo.canivalesizq=nuevo.canivalesizq-1
                nuevo.canivalesder=nuevo.canivalesder+1
            else:
                nuevo.canivalesizq=nuevo.canivalesizq+1
                nuevo.canivalesder=nuevo.canivalesder-1
        case "Mover2canibal":
            if(estado.barcaizq):
                nuevo.canivalesizq=nuevo.canivalesizq-2
                nuevo.canivalesder-=nuevo.canivalesder+2
            else:
                nuevo.canivalesizq=nuevo.canivalesizq+2
                nuevo.canivalesder-=nuevo.canivalesder-2
        case "Mover1canibal1misionero":
            if(estado.barcaizq):
                nuevo.canivalesizq=nuevo.canivalesizq-1
                nuevo.canivalesder=nuevo.canivalesder+1
                nuevo.misionerosizq=nuevo.misionerosizq-1
                nuevo.misionerosder=nuevo.misionerosder+1
            else:
                nuevo.canivalesizq=nuevo.canivalesizq+1
                nuevo.canivalesder=nuevo.canivalesder-1
                nuevo.misionerosizq=nuevo.misionerosizq+1
                nuevo.misionerosder=nuevo.misionerosder-1
        case "Mover1misionero":
            if(estado.barcaizq):
                nuevo.misionerosizq=nuevo.misionerosizq-1
                nuevo.misionerosder=nuevo.misionerosder+1
            else:
                nuevo.misionerosizq=nuevo.misionerosizq+1
                nuevo.misionerosder=nuevo.misionerosder-1
        case "Mover2misionero":
            if(estado.barcaizq):
                nuevo.misionerosizq=nuevo.misionerosizq-2
                nuevo.misionerosder=nuevo.misionerosder+2
            else:
                nuevo.misionerosizq=nuevo.misionerosizq+2
                nuevo.misionerosder=nuevo.misionerosder-2

    return nuevo

def heuristica(estado:tEstado) -> int:
    return estado.canivalesizq+estado.misionerosizq

