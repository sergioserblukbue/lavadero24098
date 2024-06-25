import os 
import json

#funciones
def limpiarPantalla():
    os.system("cls" if os.name == "nt" else "clear")
    return
def cargarDatos():
    try:
        with open("./data/vehiculos.json","r") as file: #r/read w/write x/creacion a/update
            return json.load(file)
    except:
        return {}
def guardarDatos(vehiculos):
    with open("./data/vehiculos.json","w") as file:
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

def entregarVehiculos(vehiculos):
    limpiarPantalla()
    print("Entrega de vehiculos".center(50," ") )
    patente=input("ingrese la matricula del vehiculo a entregar: ")
    if patente in vehiculos:
        vehiculo=vehiculos["patente"]
        print(f"vehiculo estado: {vehiculo['estado']}")
        if vehiculo["estado"]=="listo":
            vehiculo["estado"]="entregado"
            print("vehiculo listo para entregar!")
            guardarDatos(vehiculos)
        elif vehiculo["estado"]=="entregado":
            print("el vehiculo ya ha sido entregado!")
    else:
        print("el vehiculo no esta registrado!")
    return
def modificarEstado(vehiculos):
    print("Modificar estados".center(50," "))
    patente=input("ingrese la patente del vehiculo: ")
    if patente in vehiculos:
        print(f"matricula: {patente} estado: {vehiculos[patente]['estado']}")
        estado=input("ingrese el nuevo estado: en proceso/terminado/entregado: ")
        vehiculos[patente]["estado"]=estado
        print("estado modificado correctamente!")
        guardarDatos(vehiculos)
        input("presione enter para continuar")
    else:
        print("vehiculo no registrado!")
        input("presione enter para continuar")
    return
def listarVehiculos(vehiculos):
    limpiarPantalla()
    print("Listar Vehiculos".center(50," "))
    print("1. listar todos")
    print("2. listar pendientes")
    print("3. listar terminados")
    print("4. listar entregados")
    print("5. ir al menu anterior")
    op = input("seleccione una opcion: ")
    if op == "1":
        limpiarPantalla()
        print("Listado completo".center(50," "))
        print("="*23)
        print("|" + "patente".center(10," ") + "|" + "estado".center(10," ") + "|")
        print("="*23)
        for pat,dic in vehiculos.items():
            print("|" + str(pat).ljust(10," ") + "|" + str(dic['estado']).ljust(10," ") + "|"  )
        print("="*23)
        input("presione enter para continuar...")
    if op =="2":
        limpiarPantalla()
        print("listado de pendientes".center(50," "))
        print("="*23)
        print("|" + "patente".center(10," ") + "|" + "estado".center(10," ") + "|")
        print("="*23)
        for pat,dic in vehiculos.items():
            if dic["estado"]=="pendiente":
                print("|" + str(pat).ljust(10," ") + "|" + str(dic['estado']).ljust(10," ") + "|"  )
        print("="*23)
        input("presione enter para continuar...")
    if op =="3":
        limpiarPantalla()
        print("listado de terminados".center(50," "))
        print("="*23)
        print("|" + "patente".center(10," ") + "|" + "estado".center(10," ") + "|")
        print("="*23)
        for pat,dic in vehiculos.items():
            if dic["estado"]=="terminado":
                print("|" + str(pat).ljust(10," ") + "|" + str(dic['estado']).ljust(10," ") + "|"  )
        print("="*23)
        input("presione enter para continuar...")
    if op =="4":
        limpiarPantalla()
        print("listado de entregados".center(50," "))
        print("="*23)
        print("|" + "patente".center(10," ") + "|" + "estado".center(10," ") + "|")
        print("="*23)
        for pat,dic in vehiculos.items():
            if dic["estado"]=="entregado":
                print("|" + str(pat).ljust(10," ") + "|" + str(dic['estado']).ljust(10," ") + "|"  )
        print("="*23)
        input("presione enter para continuar...")
    return

#programa principal
limpiarPantalla()
vehiculos=cargarDatos()
while True:
    opcion = menu()
    if opcion=="1":
        ingresarVehiculo(vehiculos)
    elif opcion == "2":
        pass
        entregarVehiculos(vehiculos)
    elif opcion=="3":
        listarVehiculos(vehiculos)
    elif opcion=="4":
        modificarEstado(vehiculos)
    elif opcion=="5":
        break
    else:
        input("opcion no valida! presione enter para continuar...")
