#Autores: Erick Alexander Barrera Ochoa y Aroldo Xavier López Osoy // 03/03/2022

#Se importa turtle junto con sus funciones
import turtle
from turtle import *

#Se indica que utilizaremos el cursor para dibujar
pen()

#Se le asigna la velocidad de turtle a 1, para que cuando se realice el gráfico se pueda apreciar
speed(2)

#Se realizan movimientos para tener suficiente espacio para dibujar la figura. El pincel se levanta.
up()
left(180)
forward(100)

#Se declaran contadores, que nos servirán para gráficar 2 cuadrados y 2 hexágonos
contador = 0
contador1 = 0
contador2 = 0
contador3 = 0

#El pincel se baja para poder empezar a realizar el trazo.
down()

#Se grafica el cuadrado. Se le asigna un color y se comienza el llenado.
fillcolor('#744700')
begin_fill()

#while que nos permitira dibujar el cuadrado
while contador < 4:
        forward(100)
        left(90)
        contador = contador + 1
   
#Se termina el llenado.   
end_fill()


#Se grafica el hexagono. Se le asigna un color y se comienza el llenado.
fillcolor('#274e12')
begin_fill()
#while que nos permitira dibujar el hexágono
while(contador1 < 6):
    forward(100)
    right(60)
    contador1 = contador1 + 1
#Se termina el llenado.
end_fill()

#Se grafica el triángulo. Se le asigna un color y se comienza el llenado.
fillcolor('#8e581f')
begin_fill()

#Se realizan los movimientos para dibujar el triángulo.
left(180)
forward(100)
left(120)
forward(100)
left(120)
forward(101)

#Se termina el llenado.
end_fill()

#Levantamos y reposicionamos el pincel.
left(120)
up()
forward(100)

#Bajamos el pincel
down()

#Se grafica el hexágono. Se le asigna un color y se comienza el llenado
fillcolor('#274e12')
begin_fill()

#while que nos permitira dibujar el hexágono
while(contador2 < 6):
    forward(100)
    left(60)
    contador2 = contador2 + 1
#Se termina el llenado.
end_fill()

#Se grafica el cuadrado. Se le asigna un color y se comienza el llenado.
fillcolor('#744700')
begin_fill()
right(90)
#while que nos permitira dibujar el cuadrado.
while contador3 < 4:
        forward(100)
        left(90)
        contador3 = contador3 + 1
#Se termina el llenado 
end_fill()

#Levantamos y reposicionamos el pincel para poder seguir con el dibujo.
up()
left(180)
forward(172.5)
left(90)

#Bajamos el pincel.
down()

#Se grafica el triángulo. Se le asigna un color y se comienza el llenado.
fillcolor('#8e581f')
begin_fill()

#Se realizan los movimientos para graficar el triángulo.
forward(100)
left(120)
forward(100)
left(120)
forward(100)

#Se termina el llenado.
end_fill()

#Levantamos y reposicionamos el pincel.
up()
right(60)
forward(100)

#Bajamos el pincel.
down()

#Se grafica el triángulo. Se le asigna un color y se comienza el llenado.
fillcolor('#8e581f')
begin_fill()

#Se realizan los movimientos para graficar el triángulo.
forward(100)
right(120)
forward(100)
right(120)
forward(100)

#Se termina el llenado.
end_fill()

#Levantamos y reposicionamos el pincel.
up()
right(180)
forward(100)

#Bajamos el pincel.
down()

#Se grafica el triángulo. Se le asigna un color y se comienza el llenado.
fillcolor('#fff1cc')
begin_fill()

#Se realizan los movimientos para dibujar el triángulo.
forward(100)
left(120)
forward(100)
left(120)
forward(100)

#Se termina el llenado.
end_fill()

#Levantamos y reposicionamos el pincel.
up()
left(180)
forward(100)

#Bajamos el pincel.
down()

#Se grafica el triángulo. Se le asigna un color y se comienza el llenado.
fillcolor('#fff1cc')
begin_fill()

#Se realizan los movimientos para dibujar el triángulo.
forward(100)
right(120)
forward(100)
right(120)
forward(100)
right(120)

#Se termina el llenado.
end_fill()

#Levantamos y reposicionamos el pincel.
up()
forward(100)
left(120)

#Bajamos el pincel.
down()

#Se grafica el trapecio. Se le asigna un color y se comienza el llenado.
fillcolor('#47b30f')
begin_fill()

#Se realizan los movimientos para dibujar el trapecio.
forward(100)
left(60)
forward(100)
left(60)
forward(100)
left(120)
forward(200)

#Se termina el llenado.
end_fill()

#Se levanta y reposiciona el pincel.
up()
left(120)
forward(100)
left(60)
forward(100)

#Bajamos el pincel.
down()

#Se grafica el triángulo. Se le asigna un color y se comienza el llenado.
fillcolor('#ce7e00')
begin_fill()

#Se realizan los movimientos para dibujar el triángulo.
forward(100)
right(120)
forward(100)
right(120)
forward(100)
right(120)

#Se termina el llenado.
end_fill()

#Se levanta, reposiciona y se baja el pincel para seguir dibujando.
up()
forward(100)
down()

#Se grafica el triángulo. Se le asigna un color y se comienza el llenado.
fillcolor('#ce7e00')
begin_fill()

#Se realizan los movimientos para dibujar el triángulo.
forward(100)
right(120)
forward(100)
right(120)
forward(100)
right(120)

#Se termina el llenado.
end_fill()

#Se levanta, reposiciona y se baja el pincel para seguir dibujando.
up()
forward(100)
down()

#Se grafica el triángulo. Se le asigna un color y se comienza el llenado.
fillcolor('#ce7e00')
begin_fill()

#Se realizan los movimientos para dibujar el triángulo.
forward(100)
right(120)
forward(100)
right(120)
forward(100)
right(120)

#Se termina el llenado.
end_fill()

#Se levanta, reposiciona y se baja el pincel para seguir dibujando.
up()
forward(100)
down()

#Se grafica el triángulo. Se le asigna un color y se comienza el llenado.
fillcolor('#ce7e00')
begin_fill()

#Se realizan los movimientos para dibujar el triángulo.
forward(100)
right(120)
forward(100)
right(120)
forward(100)
right(120)
forward(100)

#Se termina el llenado.
end_fill()

#Se grafica el paralelogramo. Se le asigna un color y se comienza el llenado.
fillcolor('#38751d')
begin_fill()

#Se realizan los movimientos para dibujar el paralelogramo.
forward(100)
left(60)
forward(100)
left(120)
forward(100)
left(60)
forward(100)
left(120)

#Se termina el llenado.
end_fill()

#Se sube, reposiciona y se baja el pincel para seguir dibujando
up()
forward(100)
down()

#Se grafica el triángulo. Se le asigna un color y se comienza el llenado.
fillcolor('#6aa74f')
begin_fill()

#Se realizan los movimientos para dibujar el triángulo.
forward(100)
left(120)
forward(100)
left(120)
forward(100)

#Se termina el llenado.
end_fill()

















