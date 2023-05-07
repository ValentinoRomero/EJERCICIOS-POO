import csv
from clase_email import Email
if __name__== '__main__':
    lista=[]
    #1
    nombre=input('Ingrese nombre: ')
    direccion=input('Ingrese direccion: ')
    mail1 = Email(None,None,None,None)
    mail1.crearCuenta(direccion)
    print(f'Estimado {nombre} te enviaremos tus mensajes a la dirección {mail1.retornaEmail()}')
    #2
    mail1.Modificarcuenta()
    mail1.Mostrarcuenta()
    #3
    direccion2=input('Ingrese direccion: ')
    mail2= Email(None,None,None,None)
    mail2.crearCuenta(direccion2)
    mail2.Mostrarcuenta()
    #4a
    archivo = open('datos.csv')
    reader = csv.reader(archivo,delimiter=',')
    for fila in reader:
        n=0
        for correo in fila:
            n+=1
            print(f'============Correo {n} ===========')
            mail3= Email(None,None,None,None)
            if mail3.crearCuenta(correo)==1 :
                lista.append(mail3)
            else:
                print(f"Correo invalido: {correo}")
    archivo.close()
    #4b
    dom=input("Ingrese dominio: ")
    cantdom=0
    for mail4 in lista:
        if mail4.getDominio() == dom:
            cantdom+=1
    print(f"La cantidad de Emails con el dominio {dom} es de: {cantdom}")
    


        
