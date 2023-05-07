from Clase_PlanAhorro import PlanAhorro
import Funciones
if __name__==("__main__"):
    lista=[]
    Funciones.CargaLista(lista)
    opcion=-1
    while opcion!=0:
        print("============MENU============")
        print("0- Salir")
        print("1- Actualizar valor")
        print("2- Vehiculos con cuota inferior")
        print("3- Mostrar monto que se debe haber pagado para licitar el vehiculo")
        print("4- Modificar cantidad de cuotas que debe tener pagas para licitar")
        opcion=int(input("Ingrese opcion: "))
        if opcion!=0:
            if opcion >4:
                print("La opcion ingresada no es valida")
            else:
                if opcion==1:
                    for plan in lista:
                        plan.Mostrar()
                        plan.ActualizarValor(int(input("Ingrese valor actual: ")))
                if opcion==2:
                    valor=int(input("Ingrese valor: "))
                    for plan in lista:
                        if valor>plan.ValorCuota():
                            plan.Mostrar()
                if opcion==3:
                     for plan in lista:
                         plan.Mostrar()
                         print(f"El monto que se debe haber pagado es: {plan.MontoAPagar()}")
                if opcion==4:
                    codigo=int(input("Ingrese codigo de plan: "))
                    monto=int(input("Ingrese nuevo monto: "))
                    lista[codigo].ModificarCuotasPagas(monto)

