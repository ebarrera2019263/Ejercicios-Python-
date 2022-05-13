## Algoritmos y programacion basica
## Luwing Cano
## Erick Barrera 22934 Allison David


## importacion de modulos csv y os
import csv
import os

## se crea la funcion leer la cual nos permite abrir los arcivos csv 
## funcion Allison 
def leer():
    print('lectura')
    with open ('temario.csv', mode='r') as archivo:
        csv_reader = csv.reader(archivo, delimiter=',')
        for row in csv_reader:
            print(row)



## se crea la funcion guardar la cual nos permite ingresar un nuevo registro 
## en nuestro archivos csv
## funcion realizada por Erick Barrera
def guardar():
        cantidad = int(input('cuantas peliculas dese registrar'))
        with open('temario.csv', 'a', newline='') as archivo:
            writer = csv.writer(archivo,delimiter=',')
            for i in range(cantidad):
                os.system('cls')
                Nombre = input('nombre: ')
                Estado = input('estado: ')
                Duracion = input('duracion: ')
                Capitulos = input('capitulos: ')
                Plataforma = input('paltaforma: ')
                Tiempo = input('tiempo: ')
                writer.writerow([Nombre,Estado,Duracion,Capitulos,Plataforma,Tiempo])
            print('su serie ha sido guardada con exito')



## se crea la funcion actualzar capitulo en la cual le pide al usuario
## ingresar el nombre de la serie que necesita cambiar el numero de capitulos
def actualizarCap():
    datos = []
    print('actualizar los capitulos de la serie:')
    print(' de que serie desea actualizar:')
    serien = input('')
    with open ('temario.csv', mode='r') as archivo:
            csv_reader = csv.DictReader(archivo)
            for row in csv_reader:
                datos.append(dict(row))
    #print(datos)
## se agregan dos contadores uno para poder buscar el nombre
## de la serie y el otro para buscar el capitulo a actualizar 
    cont = 0
    temp = 0
    for serie in datos:
        if serie["Nombre Serie"] == serien:
            print(serie)
            temp = cont
        cont += 1
        print(cont)
    print(temp)    
    print('ingrese el numero de nuevos capitulos: ')
    datos[temp]['Capitulos vistos'] =input('')


    #print(datos)

    with open ('temario.csv', mode='w') as archivo:
            columnas = ['Nombre Serie','Estado','Duracion capitulo','Capitulos vistos','Plataforma','Tiempo invertido']
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            for row in datos:
                escritor.writerow(row)
                
            print('la serie se ha actualizado')


## esta funcion nos permite actualizar es estado de las serie qu estamos viendo 
def actualizarEstado():
    datos = []
    print('actualizar el estado de los capitulos de la serie:')
    print(' de que serie desea actualizar el estado:')
    estad = input('')
    with open ('temario.csv', mode='r') as archivo:
            csv_reader = csv.DictReader(archivo)
            for row in csv_reader:
                datos.append(dict(row))
    #print(datos)

    cont = 0
    temp = 0
    for serie in datos:
        if serie["Nombre Serie"] == estad:
            print(serie)
            temp = cont
        cont += 1
        print(cont)
    print(temp)    
    print('ingrese nuevo estado de la serie: ')
    datos[temp]['Estado'] =input('')


    #print(datos)

    with open ('temario.csv', mode='w') as archivo:
            columnas = ['Nombre Serie','Estado','Duracion capitulo','Capitulos vistos','Plataforma','Tiempo invertido']
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            for row in datos:
                escritor.writerow(row)
                
            print('la serie se ha actualizado')






## este es el menu que despliega las diferentes opciones       

def menu():
    print("**Bienvenido a nuestra aplicacion del cine**")
    opcion = input("1. desea leer el archivo con los datos actualmente guardados\n2. Agregar un nuevo registro\n3. editar capitulos \n4.editar estado \n5. Salir")
    return opcion   


while True:
    
    opcion = menu()

    if opcion == "1":
        print("leer")
        leer()
    
    elif opcion == "2":
        print("guardar....")
        guardar()

    elif opcion == "3":
        print("actualizar capitulos....")
        actualizarCap()

    elif opcion == "4":
        print("actualizar estado....")
        actualizarEstado()
    
    elif opcion == "5":
        print("cerrando programa.....")
        break
    else:
        print("Elija una de las opciones del menu")


