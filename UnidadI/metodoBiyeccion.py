import numpy as np
import matplotlib.pyplot as plt
import math

"""Ejecucion del metodo de Biyeccion"""

#Metodo que recibe un valor para la funcion que definamos
def eval_func(xi: float) ->(float): #Esta funcion recibe el punto en que se va evaluar la funcion como flotante
    return (math.tan(xi) - (4*xi))      #Funcion : tan(x) -4x

#Definicion de los limites inferior y superior
ei = -0.3
es = 0.5

while (es-ei)>1.e-3:    #Se sigue recortanto el intervalo mientras se cumpla la tolerancia del error
    if eval_func(ei) * eval_func((ei+es)/2)<0:
        es = (ei+es)/2
    else:
        ei=(ei+es)/2

sol = (ei+es)/2     #La solucion es la mitad del ultimo intervalo
sol = "{:.4e}".format(sol)      #formateo del numero flotante a notacion cientifca, el valor entre parentesis
print("Solucion: "+str(sol))    #genera le indica cuantos decimales tomar

"""Graficacion de la funcion"""

"""Para graficar se generan los puntos para x, y"""
x = np.linspace(-1,1,50)    #Creacion de los valores de x: ese metodo almacena 50 numeros en un vector desde -1 a 1   (limite inferior, limite superior,cantidad de muestras)
y =[]      #Definicion de una lista para los valores de y

for index in x:     #Ciclo que agrega los valores la lista y
    y.append(eval_func(index))

plt.plot(x,y)
plt.show()


