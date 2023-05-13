from deportista import Deportista
from persona import Persona

class Futbolista(Persona,Deportista):
    listaFutbolista = []
    def __init__(self,nombre,edad,altura,sexo,añosPracticando,golesMarcados,tarjetasRojas,piernaHabil):
        self._golesMarcados= golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,añosPracticando)
        Futbolista.listaFutbolista.append(self)
    
    def getGolesMarcados(self):
        return self._golesMarcados
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def getPiernaHabil(self):
        return self._piernaHabil
    

    def getAñosPracticando(self):
        return super().getAñosPracticando()
    def getAltura(self):
        return super().getAltura()
    def getDeporte(self):
        return super().getDeporte()
    def getEdad(self):
        return super().getEdad()
    def getNombre(self):
        return super().getNombre()
    def getSexo(self):
        return super().getSexo()
    
    def setGolesMarcados(self,golesMarcados):
        self._golesMarcados = golesMarcados
    def setTarjetasRoja(self,tarjetasRoja):
        self._tarjetasRoja = tarjetasRoja
    def setPiernaHabil(self,piernaHabil):
        self._piernaHabil = piernaHabil


    def setAltura(self, altura):
        return super().setAltura(altura)
    def setAñosPracticando(self, añosPracticando):
        return super().setAñosPracticando(añosPracticando)
    def setDeporte(self, deporte):
        return super().setDeporte(deporte)
    def setEdad(self, edad):
        return super().setEdad(edad)
    def setNombre(self, nombre):
        return super().setNombre(nombre)
    def setSexo(self, sexo):
        return super().setSexo(sexo)

    
    
    def __str__(self):
        return f"Mi nombre es {self.getNombre} soy profesional en el deporte {self.getDeporte} Tengo {self.getEdad} años de edad y llevo {self.getAñosPracticando} años en el deporte"
    
    

