from Clase_ViajeroFrecuente import ViajeroFrecuente
import csv

if __name__ == "__main__":
    
    listaViajeros = []
    archivo = open("viajeros.csv")
    reader = csv.reader(archivo, delimiter = ",")
    for fila in reader: 
        viajero = ViajeroFrecuente(int(fila[0]), int(fila[1]), fila[2] , fila[3] , int(fila[4]))
        listaViajeros.append(viajero)
    archivo.close()
    
    if listaViajeros[1] == 200:
        print("Es igual por izquierda \n")
    if 200 == listaViajeros[1]:
        print("Es igual por derecha \n")
    
    listaViajeros[1] = listaViajeros[1] + 100
    listaViajeros[1].MostrarDatos()
    listaViajeros[1] = 100 + listaViajeros[1]
    listaViajeros[1].MostrarDatos()

    listaViajeros[1] = listaViajeros[1] - 100
    listaViajeros[1].MostrarDatos()
    listaViajeros[1] = 100 - listaViajeros[1] 
    listaViajeros[1].MostrarDatos()
    