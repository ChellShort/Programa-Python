import os
import msvcrt

from funciones import *

print("Presione 'q' para continuar...")
key = None
while key != 'q':
    key = msvcrt.getwch()

idplaceholder = 0

registros= []

while True:
    print("1. Alta de registro\n2. Baja de registro\n3. Actualización de registro\n4. Mostrar registros\n5. Mostrar precio promedio de los productos\n6. Mostrar la cantidad de bebidas por marca\n7. Mostrar la cantidad de bebidas por clasificación\n8. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        os.system("cls")
        idplaceholder += 1
        alta(registros, idplaceholder)
    elif opcion == "2":
        os.system("cls")    
        baja(registros)
    elif opcion == "3":
        os.system("cls")
        actualizar(registros)
    elif opcion == "4":
        os.system("cls")
        mostrar(registros)
    elif opcion == "5":
        os.system("cls")
        precioProm(registros)
    elif opcion == "6":
        os.system("cls")
        cantBebidasMarca(registros)
    elif opcion == "7":
        os.system("cls")
        cantBebidasClasificacion(registros)
    elif opcion == "8":
        os.system("cls")
        break
    else:
        print("Opción inválida. Intente nuevamente.")