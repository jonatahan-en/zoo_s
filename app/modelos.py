from enum import Enum, auto


class TipoEntrada(Enum):
    BEBE = auto ()
    NIÑO = auto ()
    ADULTO = auto()
    JUBILADO = auto()

class Entrada:
    def __init__(self,edad:int):
        self.__validate_edad(edad)
        self.__edad = edad
        if edad <= 2:
            self.tipo = TipoEntrada.BEBE
            self.precio = 0
        elif edad < 13:
            self.tipo = TipoEntrada.NIÑO
            self.precio = 14
        elif edad < 65:
            self.tipo = TipoEntrada.ADULTO
            self.precio = 23
        else:
            self.tipo = TipoEntrada.JUBILADO
            self.precio = 18

    def __validate_edad(self, edad):
        if edad < 0:
            raise ValueError("la edad no debe ser negativa")


      
class Grupo_Entrada:
    def __init__(self):
        self.total = 0
        self.num_entradas = 0 
        self.tipos_entrada = {
             TipoEntrada.BEBE: {"Cantidad": 0, "Precio": 0},
             TipoEntrada.NIÑO: {"Cantidad":  0,  "Precio": 14},
             TipoEntrada.ADULTO: {"Cantidad":  0,  "Precio": 23},
             TipoEntrada.JUBILADO: {"Cantidad": 0,  "Precio":  18}

        }

    def add_entrada(self,edad):
       
       nueva_entrada = Entrada(edad)
       self.num_entradas += 1
       self.total += nueva_entrada.precio
        
       self.tipos_entrada[nueva_entrada.tipo]["Cantidad"] += 1
    
    def cantidad_entradas_por_tipo(self, tipo: TipoEntrada)->int:
        return self.tipos_entrada[tipo]["Cantidad"]
    
    def subtotal_tipo(self,tipo:TipoEntrada) ->int:
        return self.tipos_entrada[tipo]["Cantidad"] * self.tipos_entrada[tipo]["Precio"]