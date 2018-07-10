import os
import shutil

opciones = {1: 'Borrar carpetas', 2: 'Borrar ficheros', 3: 'Mover ficheros', 4: 'Renombrar fichero', 5: 'Listar ficheros'}

# functions:

def introduccion():
    opcion = int(input("Elige una de las opciones: \n 1 -> Borrar carpetas\n 2 -> Borrar ficheros\n "
          "3 -> mover ficheros\n 4 -> renombrar fichero\n 5 -> Listar ficheros \n opcion: "))
    return opcion

def borrarCarpeta(carp_borrar):
    permiso = input('¿Estas seguro?(y/n)')
    if permiso == 'y':
        os.rmdir(carp_borrar)
    else:
        print('Has decidido cancelar')

def borrarArchivo(arch_borrar):
    if os.path.exists(arch_borrar) == True:
        permiso = input('¿Estas seguro?(y/n)')
        if permiso == 'y':
            os.remove(arch_borrar)
        else:
            print('Has decidido cancelar')
    else:
        print('El archivo no existe')

def movFich():
    try:
        ruta_origen = input('Introduzca la ruta de origen y el nombre del fichero: ')
        ruta_destino = input('Introduzca la ruta de destino y el nombre del fichero: ')
        shutil.move(ruta_origen, ruta_destino)
    except FileNotFoundError:
        print('Alguno de los directorios o ficheros')

def rename():
    ruta_fichero = input('Introduzca la ruta: ')
    if os.path.isdir(ruta_fichero) == True:
        print('Estamos en : ', ruta_fichero)
        ficheros = os.listdir(ruta_fichero)

        for fichero in ficheros:
            print(fichero)

            fichero_elegido = input('Elija un fichero: ')
            if os.path.isfile(fichero_elegido) == True:
                ruta_fichero_original = ruta_fichero + fichero_elegido
                nombre_nuevo = input('Ingrese un nuevo nombre: ')
                nombre_nuevo = ruta_fichero + nombre_nuevo
                print(nombre_nuevo)
                os.rename(ruta_fichero_original, nombre_nuevo)
            else:
                print('El fichero no existe')
                break
        else:
            print('la ruta no existe')

def listar(carpeta):
    print('En el directorio actual existen los siguientes ficheros: \n', os.listdir(carpeta))

def listar_directorio():
    print('')

confir = 'Y'
while confir == 'Y':
    try:
        opcion = introduccion()
        if opcion < 1 or opcion > len(opciones):
            print('La opcion no existe')
            introduccion()
        else:
            if opcion == 5:
                carpeta = input('¿Que carpeta quieres listar?')
                if os.path.exists(carpeta) == True:
                    listar(carpeta)
                else:
                    print('La carpeta no existe')
            elif opcion == 1:
                carp_borrar = input('¿introduzca la carpeta que deseas borrar: ')
                if os.path.exists(carp_borrar) == True:
                    borrarCarpeta(carp_borrar)
                else:
                    print('La carpeta no existe')
            elif opcion == 2:
                arch_borrar = input('¿introduzca la ruta y nombre del archivo que deseas borrar: ')
                borrarArchivo(arch_borrar)
            elif opcion == 3:
                movFich()
            elif opcion == 4:
                rename()
            else:
                print('Esta opcion no existe')
        confir = input("¿Desea volver a ejecutar el script?('Y/N')")
    except ValueError:
        print("La opcion no es valida.")
        confir = input("¿Quieres volver a ejecutar el script?('Y/N')")
