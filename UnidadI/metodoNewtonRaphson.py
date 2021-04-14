
"""
    Autor: Roberto Sánchez Núñez
    NC: 18420488
    Actividad: Método de Newton-Raphson
"""

import sympy as sp
import math

xi=0    #Valor inicial de evaluación
x= sp.symbols('x')

fx = (math.e**-x)-x     #Defino la función para realizar la integral

def eval_func(valor):   #Método que evalua la función en el punto dado
    return ((math.e**-valor)-valor)

def evalaucion_func_diff(valor):    #Método que deriva la función en el punto dado
    return sp.diff(fx,x).subs(x,valor)

error=100       #Valor con el que inica el error relativo

while(error>1.e-8):        #Ciclo que realiza la recursividad del metodo hasta 10^-8
    valorCalc=xi;           #Obtengo el valor de xi para calcular su % de error antes de ser alterado
    xi = xi-(eval_func(xi)/evalaucion_func_diff(xi))    #Genera el nuevo xi
    error = ((xi - valorCalc)/xi)*100
    print("Error realtivo de: "+("%.9f" % valorCalc)+" --> "+("{:.6e}".format(error)))

print("Solucion : "+("%.9f" % xi))
