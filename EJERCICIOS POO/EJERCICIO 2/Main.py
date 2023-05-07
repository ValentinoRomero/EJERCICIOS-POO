from Clase_ViajeroFrecuente import ViajeroFrecuente
import csv

if  __name__ == "__main__":
    lista=[]
    archivo = open('datos1.csv')
    reader = csv.reader(archivo,delimiter=',')
    for fila in reader:
         viajero=ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3],fila[4])
         lista.append(viajero)
    archivo.close()
    opcion=-1
    while opcion != 0:
          print("========Menu========")
          print("0- Salir")
          print("1- Consultar cantidad de millas")
          print("2- Acumular Millas")
          print("3- Canjear Millas")
          opcion=int(input("Ingrese opcion: "))
          if opcion != 0:
               numviajero=int(input("Ingrese numero de viajero: "))
               if numviajero > len(lista):
                    print("No se encontro el Viajero")
               else:

                    if opcion == 1:
                         print(f"Cantidad de millas {lista[int(numviajero-1)].cantidadTotalMillas()}")
                    else:
                         if opcion==2:
                              millas=int(input("Ingrese Millas a acumular: "))
                              lista[numviajero-1].acumularMillas(millas)
                         else:
                              if opcion==3:
                                   millas= int(input("Ingrese cantidad de Millas a canjear: "))
                                   lista[numviajero-1].canjearMillas(millas)
                              else: 
                                   print("La opcion que ingreso no existe")






    