class Conjunto:
    
    def _init_(self):
        self.__lista=[]
        
    def cargaLista(self):
        elemento=int(input("ingrese un elemento a cargar \n"))
        while elemento != 0:
            self.__lista.append(elemento)
            elemento=int(input("ingrese un elemento a cargar 0 para terminar \n"))
    
    def mostrar(self):
        return self.__lista
        
    def agregar(self,elemento):
            self.__lista.append(elemento)
    
    def ordena(self):
        return self.__lista.sort()
        
    def _add_(self,otro):
        for y in otro.__lista:
                if y not in self.__lista:
                    lista3.append(y)
        for x in self.__lista:
            lista3.append(x)       
        return lista3
    
    
    def _sub_(self,otro):
      
        for x in self.__lista:
            if x not in otro.__lista:
                lista4.append(x)
        return lista4
        
    def _eq_(self,otro):
        band=True
        if len(self._lista) != len(otro._lista):
            band=False
        else:
            for x in self.__lista:
                if x not in otro.__lista:
                    band=False
            for y in otro.__lista:
                if y not in self.__lista:
                    band=False
        return band
if __name__=='main_':
            lista1=Conjunto()
            lista2=Conjunto()
            print("----LISTA 1-----")
            lista1.cargaLista()
            print("----LISTA 2-----")
            lista2.cargaLista()
            lista1.ordena()
            lista2.ordena()
            print(f"los elementos de la lista 1 son: {lista1.mostrar()} ")
            print(f"los elementos de la lista 2 son: {lista2.mostrar()} ")
            menu=int(input("1. Union de Conjuntos \n 2. Diferencia de Conjuntos \n 3.Igualdad de Conjuntos \n 0. Salir \n"))
            while menu != 0:
                
                if menu == 1:
                    lista3=Conjunto()
                    lista3= lista1 + lista2
                    lista3.ordena()
                    print(f"{lista3.mostrar()} ")
                if menu == 2:
                    lista4=Conjunto()
                    lista4= lista1 - lista2
                    lista4.ordena()
                    print(f"{lista4.mostrar()} ")
                if menu == 3:
                    if lista1 == lista2:
                        print(" lista 1 y lista 2 son iguales")
                    else:
                        print("Las listas 1 y 2 no son iguales")
                menu=int(input("1. Union de Conjuntos \n 2. Diferencia de Conjuntos \n 3.Igualdad de Conjuntos \n 0. Salir \n"))