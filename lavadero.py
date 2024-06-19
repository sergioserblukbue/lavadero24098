import os 
import json

#funciones
def limpiarPantalla():
    os.system("cls" if os.name == "nt" else "clear")
    return
def cargarDatos():
    try:
        with open("vehiculos.json","r") as file: #r/read w/write x/creacion a/update
            return json.load(file)
    except:
        return {}
def guardarDatos(vehiculos):
    with open("vehiculos.json","w") as file:
        json.dump(vehiculos, file,indent=4)
    return
def ingresarVehiculo(vehiculos):
    limpiarPantalla()
    print("ingreso de vehiculos".center(50," "))
    patente=input("ingrese la patente: ")
    interior=input("lavado de interior s/n ")
    exterior=input("lavado de exterior s/n ")
    motor=input("lavado de motor s/n ")
    estado="pendiente"
    dniPropietario=input("ingrese el dni del propietario: ")
    vehiculos[patente]={
        "interior":interior,
        "exterior":exterior,
        "motor":motor,
        "estado":estado,
        "dniPropietario":dniPropietario
    }
    guardarDatos(vehiculos)
    return
def modificarEstado(vehiculos):
    limpiarPantalla()
    print("modificar estados".center(50," "))
    patente=input("ingrese la patente del vehiculo: ")
    if patente in vehiculos:
        print(f"patente: {patente} estado: {vehiculos[patente]['estado']}")
        estado=input("ingrese el nuevo estado: proceso/terminado/entregado: ")
        vehiculos[patente]["estado"]=estado
        guardarDatos(vehiculos)
        input("datos guardados correctamente!  enter para continuar...")
    else:
        input("vehiculo no registrado! enter para continuar")
    return
def menu():
    print("menu principal".center(50," "))
    print("""
            1. para ingresar un vehiculo
            2. para salida de vehiculos
            3. para listar vehiculos
            4. modificar estados
            5. para salir
        """)
    opcion=input("seleccione una opcion: ")
    return opcion



#programa principal
limpiarPantalla()
vehiculos=cargarDatos()
while True:
    opcion = menu()
    if opcion=="1":
        ingresarVehiculo(vehiculos)
    elif opcion == "2":
        pass
        #retirarVehiculo()
    elif opcion=="3":
        pass
        #listarVehiculos()
    elif opcion=="4":
        modificarEstado(vehiculos)
    elif opcion=="5":
        break
    else:
        input("opcion no valida! presione enter para continuar...")

