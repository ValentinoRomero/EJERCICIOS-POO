class Email:
    __idcuenta=''
    __dominio=''
    __tipodom=''        
    __contra=''
    def __init__(self,idcuenta,dominio,tipodom,contra):
        self.__idcuenta=idcuenta
        self.__dominio=dominio
        self.__tipodom=tipodom
        self.__contra=contra
    def Cargacuenta(self):
        self.__idcuenta=input('Ingrese Idcuenta: ')
        self.__dominio=input('Ingrese dominio: ')
        self.__tipodom=input('Ingrese tipo de dominio: ')
        self.__contra=input('Ingrese Contrasena: ')
    def retornaEmail(self):
        return self.__idcuenta + '@'+self.__dominio + '.' + self.__tipodom
    def getDominio(self):
        return self.__dominio
    def crearCuenta(self,direccion):
        if "@" in direccion and "." in direccion:
            partes = direccion.split("@")
            self.__idcuenta = partes[0]
            partes=partes[1].split('.')
            self.__dominio=partes[0]
            self.__tipodom=partes[1]
            self.__contra = input("Ingrese la contraseña: ")
            band=1
        else:
            band=-1
        return band
    def Mostrarcuenta(self):
        print(f'idcuenta: {self.__idcuenta}')
        print(f'dominio: {self.__dominio}')
        print(f'tipo dominio: {self.__tipodom}')
        print(f'contrasena: {self.__contra}')
    def Modificarcuenta(self):
        contra1=input('Ingrese contrasena actual: ')
        while contra1!=self.__contra:
            contra1= input('Contrasena incorrecta, ingrese nuevamente: ')
        self.__contra=input('Ingrese nueva contrasena: ')