class PlanAhorro:
    cuotas=12
    cuotas_pagas=6
    def __init__(self,codigo,modelo,version,valor):
        self.__codigo=codigo
        self.__modelo=modelo
        self.__version=version
        self.__valor=valor
    def ActualizarValor(self,valor):
        self.__valor=valor
    def ValorCuota(self):
        return float(self.__valor/self.getCuotas()+self.__valor*0.10)
    def Mostrar(self):
        print(f"Codigo: {self.__codigo}")
        print(f"Modelo: {self.__modelo}")
        print(f"Version: {self.__version}")
    def MontoAPagar(self):
        return self.getCuotasPagas()*self.ValorCuota()
    @classmethod
    def getCuotas(cls):
        return cls.cuotas
    def getCuotasPagas(cls):
        return cls.cuotas_pagas
    def ModificarCuotasPagas(cls,monto):
        cls.cuotas_pagas=monto
        