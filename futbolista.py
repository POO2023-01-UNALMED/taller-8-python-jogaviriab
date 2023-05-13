from deportista import Deportista
from persona import Persona

class Futbolista(Persona,Deportista):
    listaFutbolista = []
    def __init__(self,nombre,edad,altura,sexo,añosPracticado,golesMarcados,tarjetasRojas,piernaHabil):
        self._golesMarcados= golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Persona().__init__(self,nombre,edad,altura,sexo)
        Deportista().__init__(self,añosPracticado)
        Futbolista.listaFutbolista.append(self)
    
    def getGolesMarcados(self):
        return self._golesMarcados
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def getPiernaHabil(self):
        return self._piernaHabil
    
    def setGolesMarcados(self,golesMarcados):
        self._golesMarcados = golesMarcados
    def setTarjetasRoja(self,tarjetasRoja):
        self._tarjetasRoja = tarjetasRoja
    def setPiernaHabil(self,piernaHabil):
        self._piernaHabil = piernaHabil
    
    def __str__(self):
        return f"Mi nombre es {self.getNombre} soy profesional en el deporte {self.getDeporte} Tengo {self.getEdad} años de edad y llevo {self.getAñosPracticado} años en el deporte"
    
    

