class Registro:
    def __init__(self,temperatura:int,humedad: int,presion: float):
        self.__temp=temperatura
        self.__humedad=humedad
        self.__presion=presion
    def getTemperatura(self):
        return self.__temp
    def getHumedad(self):
        return self.__humedad
    def getPresion(self):
        return self.__presion