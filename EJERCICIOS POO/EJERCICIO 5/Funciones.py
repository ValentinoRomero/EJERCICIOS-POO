import csv
from Clase_PlanAhorro import PlanAhorro
def CargaLista(lista):
    archivo=open("planes.csv")
    reader=csv.reader(archivo,delimiter=';')
    for fila in reader:
        plan=PlanAhorro(int(fila[0]),str(fila[1]),str(fila[2]),int(fila[3]))
        lista.append(plan)
    archivo.close()
