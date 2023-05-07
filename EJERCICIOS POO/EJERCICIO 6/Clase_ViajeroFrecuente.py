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
    
    def MostrarDatos(self):
        print(f"Numero de viajero:{self.__num_viajero}\n{self.__apellido} {self.__nombre}\n Tiene {self.__millas_acum} millas acumuladas .\n Su dni es: {self.__dni}")
    
    def getNumViajero(self):
        return int(self.__num_viajero)
    
    def __add__(self, num):
        return ViajeroFrecuente(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum + num)
    
    def __gt__(self, otro):
        return self.cantidadTotalMillas() > otro.cantidadTotalMillas()
    
    def __sub__(self, num):
        return ViajeroFrecuente(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum - num)
    