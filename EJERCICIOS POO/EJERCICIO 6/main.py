from Clase_ViajeroFrecuente import ViajeroFrecuente
import csv

if __name__ == "__main__":
    listaViajeros = []
    archivo = open("viajeros.csv")
    reader = csv.reader(archivo, delimiter = ",")
    for fila in reader: 
        viajero = ViajeroFrecuente(fila[0], int(fila[1]), fila[2],fila[3], int(fila[4]))
        listaViajeros.append(viajero)
    archivo.close()
 
    viajeroMaximo = []
    
    numeroMillasMax = 0
    
    for objeto in listaViajeros:
        if objeto.cantidadTotalMillas() > numeroMillasMax:
            numeroMillasMax = objeto.cantidadTotalMillas()
    
    print ("Los viajeros con mayor cantidad de millas son: ")
    
    for objeto in listaViajeros:
        if numeroMillasMax == objeto.cantidadTotalMillas():
            objeto.MostrarDatos()
            viajeroMaximo.append(objeto)
    

    listaViajeros[1] = listaViajeros[1] + 100
    listaViajeros[1].MostrarDatos()
    
    
    listaViajeros[1] = listaViajeros[1] - 150
    listaViajeros[1].MostrarDatos() 
