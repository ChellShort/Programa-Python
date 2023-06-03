import os
import msvcrt

def alta(registros, idplaceholder):
    id = int(idplaceholder)
    nombre = (input("Ingrese el nombre: "))
    clasificacion = input("Ingrese la clasificacion: ")
    marca = input("Ingrese la marca: ")
    precio = float(input("Ingrese el precio: "))
    registro = {
        "id": id,
        "nombre": nombre,
        "clasificacion": clasificacion,
        "marca": marca,
        "precio": precio
    }
    registros.append(registro)
    print("Registro agregado con éxito.\n")

    print("Presione 'q' para continuar...")
    key = None
    while key != 'q':
        key = msvcrt.getwch()

def baja(registros):
    id = int(input("Ingrese el id del objeto a eliminar: "))

    for registro in registros:
        if registro["id"] == id:
            registros.remove(registro)
            print("Registro eliminado con éxito.")
            return
        
    print("No se encontró ningún registro con ese id.\n")

    print("Presione 'q' para continuar...")
    key = None
    while key != 'q':
        key = msvcrt.getwch()

def mostrar(registros):
    for registro in registros:
        print("id: ", registro["id"], " / Nombre: ", registro["nombre"], " / Clasificacion: ", registro["clasificacion"], " / Marca: ", registro["marca"], " / Precio: ", registro["precio"])
        print("----------------------------------------")

def actualizar(registros):
    print("1. Id")
    print("2. Nombre")
    print("3. Clasificacion")
    print("4. Marca")
    print("5. Precio")
    opcion1 = input("Ingrese un parametro por el que desea buscar: ")

    if opcion1 == "1":
        id = int(input("Ingrese el Id del registro a actualizar: "))

        for registro in registros:
            if registro["id"] == id:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                nueva_clasificacion = (input("Ingrese la nueva clasificacion: "))
                nueva_marca = input("Ingrese la nueva marca: ")
                nuevo_precio = float(input("Ingrese el nuevo precio: "))

                registro["nombre"] = nuevo_nombre
                registro["clasificacion"] = nueva_clasificacion
                registro["marca"] = nueva_marca
                registro["precio"] = nuevo_precio

                print("Registro actualizado con éxito")
                return
        print("No se encontró ningún registro con ese Id")
    elif opcion1 == "2":
        nombre = (input("Ingrese el Id del registro a actualizar: "))

        for registro in registros:
            if registro["nombre"] == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                nueva_clasificacion = (input("Ingrese la nueva clasificacion: "))
                nueva_marca = input("Ingrese la nueva marca: ")
                nuevo_precio = float(input("Ingrese el nuevo precio: "))

                registro["nombre"] = nuevo_nombre
                registro["clasificacion"] = nueva_clasificacion
                registro["marca"] = nueva_marca
                registro["precio"] = nuevo_precio

                print("Registro actualizado con éxito")
                return
        print("No se encontró ningún registro con ese Nombre")

    elif opcion1 == "3":
        clasificacion = (input("Ingrese la clasificacion del registro a actualizar: "))

        for registro in registros:
            if registro["clasificacion"] == clasificacion:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                nueva_clasificacion = (input("Ingrese la nueva clasificacion: "))
                nueva_marca = input("Ingrese la nueva marca: ")
                nuevo_precio = float(input("Ingrese el nuevo precio: "))

                registro["nombre"] = nuevo_nombre
                registro["clasificacion"] = nueva_clasificacion
                registro["marca"] = nueva_marca
                registro["precio"] = nuevo_precio

                print("Registro actualizado con éxito")
                return
        print("No se encontró ningún registro con esa Clasificacion")

    elif opcion1 == "4":
        marca = (input("Ingrese la marca del registro a actualizar: "))

        for registro in registros:
            if registro["marca"] == marca:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                nueva_clasificacion = (input("Ingrese la nueva clasificacion: "))
                nueva_marca = input("Ingrese la nueva marca: ")
                nuevo_precio = float(input("Ingrese el nuevo precio: "))

                registro["nombre"] = nuevo_nombre
                registro["clasificacion"] = nueva_clasificacion
                registro["marca"] = nueva_marca
                registro["precio"] = nuevo_precio

                print("Registro actualizado con éxito")
                return
        print("No se encontró ningún registro con esa marca")

    elif opcion1 == "5":
        precio = int(input("Ingrese el precio del registro a actualizar: "))

        for registro in registros:
            if registro["precio"] == precio:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                nueva_clasificacion = (input("Ingrese la nueva clasificacion: "))
                nueva_marca = input("Ingrese la nueva marca: ")
                nuevo_precio = float(input("Ingrese el nuevo precio: "))

                registro["nombre"] = nuevo_nombre
                registro["clasificacion"] = nueva_clasificacion
                registro["marca"] = nueva_marca
                registro["precio"] = nuevo_precio

                print("Registro actualizado con éxito")
                return
        print("No se encontró ningún registro con ese precio")

    else:
        print("Opción inválida. Intente nuevamente.")

    print("Presione 'q' para continuar...")
    key = None
    while key != 'q':
        key = msvcrt.getwch()


def precioProm(registros):
    if len(registros) == 0:
        print("No hay registros almacenados.")
        return

    sumaPrecios = 0
    for registro in registros:
        sumaPrecios += registro["precio"]

    precioProm = sumaPrecios / len(registros)
    
    print("Precio promedio:", precioProm, "\n")

def cantBebidasMarca(registros):

    if len(registros) == 0:
        print("No hay registros almacenados.")
        return

    conteo_registros = {}

    for registro in registros:
        marca = registro["marca"]
        if marca in conteo_registros:
            conteo_registros[marca] += 1
        else:
            conteo_registros[marca] = 1

    print("Número de registros por marca:")
    for marca, conteo in conteo_registros.items():
        print(marca + ":", conteo, "\n")

def cantBebidasClasificacion(registros):

    if len(registros) == 0:
        print("No hay registros almacenados.")
        return

    conteo_registros = {}

    for registro in registros:
        clasificacion = registro["clasificacion"]
        if clasificacion in conteo_registros:
            conteo_registros[clasificacion] += 1
        else:
            conteo_registros[clasificacion] = 1

    print("Número de registros por clasificacion:")
    for clasificacion, conteo in conteo_registros.items():
        print(clasificacion + ":", conteo, "\n")