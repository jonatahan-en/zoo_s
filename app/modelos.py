from enum import Enum, auto

class TipoEntrada(Enum):
    BEBE = 1
    NIÑO = 2
    ADULTO = 3
    JUBILADO = 4
    VIP = "XX"

class Entrada:
    def __init__(self):
pass
     
class Grupo_Entrada:
    def __init__(self):
        self.total = 0
        self.num_entradas = 0

    