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

def listarVehiculos(vehiculos):
    limpiarPantalla()
    print("listados".center(50," "))
    print("="*50)
    print("""
            1. para listar todos
            2. para vehiculos pendientes
            3. para vehiculos listos
            4. para vehiculos entregados
            5. para lavado completo
            6. para salir al menu anterior
        """)
    op=input("seleccione una opcion: ")
    limpiarPantalla()
    if op =="1":
        print("Listado de todos los vehiculos".center(50," "))
        print("|"+"matricula".center(10)+"|"+"dni propietario".center(17)+"|"+ "estado".center(17," ")+"|")
        print("="*48)
        for mat,vehiculo in vehiculos.items():
            print("|" + str(mat).ljust(10," ") + "|" + str(vehiculo["dniPropietario"]).ljust(17," ")+ "|"+ str(vehiculo["estado"]).ljust(17," ") + "|") 
            print("|"+ "-"*46 + "|")
        print("fin del listado!")
    elif op =="2":
        print("Listado de vehiculos pendientes".center(50," "))
        print("|"+"matricula".center(10)+"|"+"dni propietario".center(17)+"|"+ "estado".center(17," ")+"|")
        print("="*48)
        for mat,vehiculo in vehiculos.items():
            if vehiculo["estado"]=="pendiente":
                print("|" + str(mat).ljust(10," ") + "|" + str(vehiculo["dniPropietario"]).ljust(17," ")+ "|"+ str(vehiculo["estado"]).ljust(17," ") + "|") 
                print("|"+ "-"*46 + "|")
        print("fin del listado!")
    elif op =="3":
        print("Listado de vehiculos terminado".center(50," "))
        print("|"+"matricula".center(10)+"|"+"dni propietario".center(17)+"|"+ "estado".center(17," ")+"|")
        print("="*48)
        for mat,vehiculo in vehiculos.items():
            if vehiculo["estado"]=="terminado":
                print("|" + str(mat).ljust(10," ") + "|" + str(vehiculo["dniPropietario"]).ljust(17," ")+ "|"+ str(vehiculo["estado"]).ljust(17," ") + "|") 
                print("|"+ "-"*46 + "|")
        print("fin del listado!")
    elif op=="4":
        print("Listado de vehiculos entregados".center(50," "))
        print("|"+"matricula".center(10)+"|"+"dni propietario".center(17)+"|"+ "estado".center(17," ")+"|")
        print("="*48)
        for mat,vehiculo in vehiculos.items():
            if vehiculo["estado"]=="entregado":
                print("|" + str(mat).ljust(10," ") + "|" + str(vehiculo["dniPropietario"]).ljust(17," ")+ "|"+ str(vehiculo["estado"]).ljust(17," ") + "|") 
                print("|"+ "-"*46 + "|")
        print("fin del listado!")
    elif op=="5":
        print("vehiculos con lavado completo".center(50," "))
        print("|"+"matricula".center(10)+"|"+"dni propietario".center(17)+"|"+ "estado".center(17," ")+"|")
        print("="*48)
        for mat,vehiculo in vehiculos.items():
            if vehiculo["interior"]=="s" and vehiculo["exterior"]=="s" and vehiculo["motor"]=="s":
                print("|" + str(mat).ljust(10," ") + "|" + str(vehiculo["dniPropietario"]).ljust(17," ")+ "|"+ str(vehiculo["estado"]).ljust(17," ") + "|") 
                print("|"+ "-"*46 + "|")
        print("fin del listado!")
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
        pass
        listarVehiculos(vehiculos)
    elif opcion=="4":
        modificarEstado(vehiculos)
    elif opcion=="5":
        break
    else:
        input("opcion no valida! presione enter para continuar...")
