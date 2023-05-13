class Deportista:
    def __init__(self,añosPracticado):
        self._deporte="Futbol"
        self._añosPracticado=añosPracticado

    def getDeporte(self):
        return self._deporte
    def getAñosPracticado(self):
        return self._añosPracticado
    

    def setDeporte(self,deporte):
        self._deporte = deporte
    def setAñosPasados(self,añosPasados):
        self._añosPasados = añosPasados