class ViajeroFrecuente():
    def __init__(self, num_viajero: int, dni: str, nombre: str, apellido: str, millas_acum: int):
        self.__num_viajero=num_viajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=millas_acum
    def cantidadTotalMillas(self):
        return self.__millas_acum
    def acumularMillas(self, cantm:int):
        self.__millas_acum=int(self.__millas_acum)+int(cantm)
        return self.__millas_acum
    def canjearMillas(self, cantm:int):
        if int(cantm)<=int(self.__millas_acum):
            self.__millas_acum=int(self.__millas_acum)-int(cantm)
        else:
            print("Error: la cantidad de millas a canjear es mayor a la cantidad acumulada")
        return self.__millas_acum
    

