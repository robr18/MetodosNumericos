# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 07:38:37 2021

Métodos Númericos : Resolución de Ecuaciones de 2do grado por la formula general

@author: Roberto Sánchez Núñez
"""

# -*- coding: utf-8 -*-

import math

a = input("Ingresa el indice del termino x^2 :")

b = input("Ingresa el coeficiente del termino x^1 :")

c = input("Ingresa el coeficiente numerico de la ecuacion c :")

discriminante = (int(b)**2)-4*int(a)*int(c)

if discriminante == 0:
        x1 = (-1*int(b))/(2*int(a))
        x2 = (-1*(-1*int(b)))/(2*int(a))
        print ("El primer valor de x1 = "+x1)
        print ("El sgundo valor de x2 = "+x2)
else:
    if discriminante > 0:
            raiz = math.sqrt(discriminante)
            x1 = ((-1*int(b))+raiz)/(2*int(a))
            x2 = ((-1*int(b))-raiz)/(2*int(a))
            print ("El primer valor de x1 = "+str(x1))
            print ("El segundo valor de x2 = "+str(x2))
    else:
        if discriminante <0:
                discriminante = abs(discriminante)
                real = (-1*int(b))/(2*int(a))
                imaginaria = math.sqrt(discriminante)/(2*int(a))
                x1 = complex(real,imaginaria)
                x2 = complex(real,-1*imaginaria)
                print ("El primer valor complejo es x1 = "+str(x1))
                print ("El segundo valor complejo es x2 = "+str(x2))