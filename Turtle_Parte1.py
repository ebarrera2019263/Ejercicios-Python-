#Autores: Erick Alexander Barrera Ochoa y Aroldo Xavier López Osoy // 03/03/2022


#Se importa turtle junto con sus funciones
import turtle
from turtle import *

#Se indica que utilizaremos el cursor para dibujar
turtle.pen()

#Se le asigna la velocidad de turtle a 1, para que cuando se realice el gráfico se pueda apreciar
turtle.speed(1)

#Inicializando la variable que contendrá el valor del lado
longitudLado=0


#Función que recibe el parametro contador y logitud lado para poder dibujar la figura
def dibujarHexagono (contador, longitudLado):
    #Se asigna el color que tendrá el interior de la figura
    turtle.fillcolor('#fdf198')
    #Comienza el llenado
    turtle.begin_fill()
    #While que permitira gráficar la figura en base a la longitud ingresada por el usuario
    while contador < 6:
        forward(10*longitudLado)
        left(60)
        contador = contador + 1
    
#Función que permite terminar el pintado de la figura
def pintarHexagono():
    turtle.end_fill()
    
#Se inicializa la variable contador
contador = 0

#Se le da una breve explicación al usuario del programa
print("Hola! Este es un programa para dibujar un hexágono. \n¿De qué tamaño quieres que sean sus lados?\n")
#Se le pide al usuario que ingrese la longitud deseada para el lado
longitudLado = int(input(longitudLado))

#Se llaman las funciones y se valuan entorno a los valores ingresados.
dibujarHexagono(contador, longitudLado)
pintarHexagono()
    
    
