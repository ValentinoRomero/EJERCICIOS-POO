from clase_Registro import Registro
import csv
if __name__=="__main__":
    #Creacion matriz
    lista=[]
    for i in range(0,30):
        lista.append([]) 
        for j in range(0,24):
            lista[i].append([])

    #Carga con datos de archivo

    archivo = open("datos.csv")
    reader = csv.reader(archivo, delimiter =",")
    for fila in reader:
        hora = Registro(int(fila[2]),int(fila [3]),float(fila [4]))
        lista[int(fila[0])-1][int(fila [1])].append(hora)
    archivo.close()
    #Menu
    opcion=-1
    while opcion!=0:
        print("==========MENU=========")
        print("0- Salir")
        print("1- Mostrar para cada variable el día y hora de menor y mayor valor")
        print("2- Indicar la temperatura promedio mensual por cada hora")
        print("3- Listar los valores de las tres variables para cada hora del día dado")
        opcion=int(input("Ingrese opcion: "))
        if opcion!=0:
            if opcion==1:

                max_temperatura = -10
                max_presion = -10
                max_humedad = -10
                for i in range(len(lista)):
                    for j in range(len(lista[i])):
                        for obj in lista[i][j]: 
                            if obj.getTemperatura() > max_temperatura:
                                max_temperatura = obj.getTemperatura()
                                dia_max_temp = i+1
                                hora_max_temp = j
                            if obj.getPresion() > max_presion:
                                max_presion = obj.getPresion()
                                dia_max_presion = i+1
                                hora_max_presion = j
                            if obj.getHumedad() > max_humedad:
                                max_humedad = obj.getHumedad()
                                dia_max_humedad = i+1
                                hora_max_humedad = j             
                print(f"Temperatura maxima: {max_temperatura} Dia {dia_max_temp} en hora {hora_max_temp}")
                print(f"Humedad maxima: {max_humedad} Dia {dia_max_humedad} en hora {hora_max_humedad}")
                print(f"Presión maxima: {max_presion} Dia {dia_max_presion} en hora {hora_max_presion}")
                

                min_temp = 1000
                min_pres = 1000
                min_hum = 1000
                for i in range(len(lista)):
                    for i in range(len(lista)):

                        for j in range(len(lista[i])):

                            for obj in lista[i][j]:

                                if obj.getTemperatura() < min_temp:
                                    min_temp = obj.getTemperatura()
                                    dia_min_temp=i+1
                                    hora_min_temp = j
                                if obj.getPresion() < min_pres:
                                    min_pres = obj.getPresion()
                                    dia_min_presion=i+1
                                    hora_min_pres = j
                                if obj.getHumedad() < min_hum:
                                    min_hum = obj.getHumedad()
                                    dia_min_humedad=i+1
                                    hora_min_hum = j 

                print(f"Temperatura mínima: {min_temp} Dia {dia_min_temp} en hora {hora_min_temp}")
                print(f"Humedad mínima: {min_hum} Dia {dia_min_humedad} en hora {hora_min_hum}")
                print(f"Presión mínima: {min_pres} Dia {dia_min_presion} en hora {hora_min_pres}")
            if opcion==2:
                for j in range(0,24):
                    acum_temp=0
                    cant=0
                    for i in range(0,30):
                        for hora in lista[i][j]:
                            acum_temp=acum_temp+hora.getTemperatura()
                    print(f"Temperatura promedio de la hora {j}: {acum_temp/i+1}")
            if opcion==3:
                dia = int(input("Ingrese el dia a listar: "))
                print("Hora          Temperatura          Humedad          Presion")
                for j in range(len(lista[dia-1])):
                    for obj in lista[dia-1][j]:
                        print(f"{j}                  {obj.getTemperatura()}                {obj.getHumedad()}             {obj.getPresion()}")
        