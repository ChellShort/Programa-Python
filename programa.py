
def alta(registros):
    id = int(input("Ingrese el id: "))
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
    print("Registro agregado con éxito.")

def baja(registros):
    id = int(input("Ingrese el id del objeto a eliminar: "))

    for registro in registros:
        if registro["id"] == id:
            registros.remove(registro)
            print("Registro eliminado con éxito.")
            return
        
    print("No se encontró ningún registro con ese id.")

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
    else:
        print("Opción inválida. Intente nuevamente.")


registros= []

while True:
    print("1. Alta de registro")
    print("2. Baja de registro")
    print("3. Actualización de registro")
    print("4. Mostrar registros")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        alta(registros)
    elif opcion == "2":
        baja(registros)
    elif opcion == "3":
        actualizar(registros)
    elif opcion == "4":
        mostrar(registros)
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Intente nuevamente.")